from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer,MyTokenObtainPairSerializer,PasswordResetSerializer,PasswordResetConfirmSerializer,PasswordChangeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import ProfileSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.mail import send_mail
from django.utils.encoding import force_bytes

class RegistrationApi(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginApi(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": "Invalid username or password. Please try again."}, status=status.HTTP_401_UNAUTHORIZED)

        data = {
            "access": serializer.validated_data.get("access"),
            "refresh": serializer.validated_data.get("refresh"),
            "user": {
                "id": serializer.validated_data.get("user_id"),
                "username": serializer.validated_data.get("username"),
                "email": serializer.validated_data.get("email"),
                "message": "User logged in successfully."
            }
        }
        return Response(data, status=status.HTTP_200_OK)

class ProfileApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = f"http://127.0.0.1:8000/password_reset/{uid}/{token}/"
                
                send_mail(
                    'Password Reset Request',
                    f'Please use the link below to reset your password: {reset_url}',
                    'neha.nimje.5057@gmail.com',
                    ['neha@gmail.com'],
                    fail_silently=False,
                )
            return Response({'detail': 'Password reset email has been sent.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data['uid']
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']

            try:
                uid = urlsafe_base64_decode(uid).decode()
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if user and default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                return Response({'detail': 'Password has been reset.'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid token or user ID.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({'detail': 'Authentication required'}, status=status.HTTP_403_FORBIDDEN)

        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not user.check_password(old_password):
                return Response({'detail': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

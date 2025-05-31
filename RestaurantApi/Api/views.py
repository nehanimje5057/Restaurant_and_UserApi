from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import MenuItem


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class LikeRestaurantView(APIView):
    def post(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        if restaurant.likes.filter(id=request.user.id).exists():
            restaurant.likes.remove(request.user)
        else:
            restaurant.likes.add(request.user)
        return Response(status=status.HTTP_200_OK)

class LikeMenuItemView(APIView):
    def post(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        if menu_item.likes.filter(id=request.user.id).exists():
            menu_item.likes.remove(request.user)
        else:
            menu_item.likes.add(request.user)
        return Response(status=status.HTTP_200_OK)

class SaveMenuItemView(APIView):
    def post(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        profile = request.user.profile
        if profile.saved_items.filter(id=menu_item.id).exists():
            profile.saved_items.remove(menu_item)
        else:
            profile.saved_items.add(menu_item)
        return Response(status=status.HTTP_200_OK)


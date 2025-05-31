"""
URL configuration for RestaurantApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/',views.RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/like/',views.LikeRestaurantView.as_view(), name='like-restaurant'),
    path('menu_items/<int:pk>/like/',views.LikeMenuItemView.as_view(), name='like-menu-item'),
    path('menu_items/<int:pk>/save/',views.SaveMenuItemView.as_view(), name='save-menu-item'),
]


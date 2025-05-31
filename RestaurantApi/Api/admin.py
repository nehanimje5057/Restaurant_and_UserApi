from django.contrib import admin
from .models import Restaurant,MenuItem,Profile
# Register your models here.

# @admin.register(Restaurant)
# class RestaurantAdmin(admin.ModelAdmin):
#     list_display = ['name','Address','owner','likes']

# @admin.register(MenuItem)
# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = ['Restaurant','name','price','likes']

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user','saved_items']


admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Profile)


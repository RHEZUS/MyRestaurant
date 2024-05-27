from rest_framework import serializers
from .models import Menus
from Restaurant.models import Restaurant
from MenuCategory.models import MenuCategory


class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menus
        fields = ['id', 'name', 'desc', 'restaurant', 'category', 'price', 'image', 'is_available']
        #read_only_fields = ['id', 'restaurant', 'category', 'price', 'image', 'is_available']
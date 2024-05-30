from rest_framework import serializers
from .models import Menus

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ['id', 'name', 'slug','desc', 'restaurant', 'category', 'price', 'image', 'is_available']

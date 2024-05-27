from rest_framework import serializers
from .models import Menu, Restaurant, Category


class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'desc', 'restaurant', 'category', 'price', 'image', 'is_available']
        #read_only_fields = ['id', 'restaurant', 'category', 'price', 'image', 'is_available']
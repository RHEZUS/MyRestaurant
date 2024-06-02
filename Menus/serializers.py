from rest_framework import serializers
from .models import Menus
from MenuCategory.serializers import MenuCategorySerializer
from MenuCategory.models import MenuCategory

class MenuSerializer(serializers.ModelSerializer):

    category_id = serializers.PrimaryKeyRelatedField(queryset=MenuCategory.objects.all(), source='category')
    category = MenuCategorySerializer(read_only=True)
    class Meta:
        model = Menus
        fields = ['id', 'name', 'desc', 'restaurant', 'category', 'category_id', 'price', 'image', 'is_available']

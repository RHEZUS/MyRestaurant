from rest_framework import serializers
from .models import MenuCategory
from users.serializers import UserSerializer

class MenuCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'desc', 'user']

from rest_framework import serializers
from .models import Restaurant
from users.serializers import UserSerializer
from Menus.serializers import MenuSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'user', 'location', 'logo_url', 'logo', 'qr_code', 'desc', 'menus']
        read_only_fields = ['id', 'qr_code']

from rest_framework import serializers
from .models import Restaurant, User, Menu

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # include relevant fields

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'slug', 'desc', 'price', 'image', 'is_available'] 

class RestaurantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    menus = MenuSerializer(many=True, read_only=True, source='menu_set')
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'desc', 'logo_url', 'location', 'qr_code', 'user', 'menus']
        read_only_fields = ['id', 'qr_code']
    
    #def create(self, validated_data):
    #    request = self.context.get('request', None)
    #    user = request.user if request else None
    #    return Restaurant.objects.create(user=user, **validated_data)

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.middleware import AdminRoleMiddleware
#from qr_code import qrcode
import qrcode
import qrcode.constants
from django.core.files.base import ContentFile
from io import BytesIO
from django.core.files import File
from qr_code.qrcode.utils import QRCodeOptions




@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_list(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.filter(user=request.user)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            restaurant = serializer.save(user=request.user)

            # Generate the QR code
            qr_data = f'http://localhost:5173/restaurant/{restaurant.id}/menus/'
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            qr_code_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            # Create a BytesIO buffer to temporarily store the image
            buffer = BytesIO()
            qr_code_image.save(buffer, format="PNG")
            buffer.seek(0)
            restaurant.qr_code.save(f'restaurant_{restaurant.id}_qrcode.png', ContentFile(buffer.getvalue()), save=False)
            
            # Save again to ensure qr_code field is updated
            restaurant.save()

            return Response(RestaurantSerializer(restaurant).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk, user=request.user)
    
    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            restaurant = serializer.save()

            # Generate and save the new QR code image
            qr_data = f'http://localhost:5173/restaurant/{restaurant.id}/menus/'
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            qr_code_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            # Create a BytesIO buffer to temporarily store the image
            buffer = BytesIO()
            qr_code_image.save(buffer, format="PNG")
            buffer.seek(0)
            restaurant.qr_code.save(f'restaurant_{restaurant.id}_qrcode.png', ContentFile(buffer.getvalue()), save=False)

            # Save again to ensure qr_code field is updated
            restaurant.save()

            return Response(RestaurantSerializer(restaurant).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Check if the restaurant has a logo, delete it if exists
        if restaurant.logo:
            restaurant.logo.delete(save=True)
        
        # Check if the restaurant has a QR code image, delete it if exists
        if restaurant.qr_code:
            restaurant.qr_code.delete(save=True)
        
        # Delete the restaurant object
        restaurant.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

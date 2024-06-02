from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Menus
from .serializers import MenuSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from Restaurant.models import Restaurant
from Restaurant.serializers import RestaurantSerializer
from MenuCategory.models import MenuCategory
from MenuCategory.serializers import MenuCategorySerializer

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def menu_list(request):
    if request.method == 'GET':
        menus = Menus.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def menu_detail(request, pk):
    menu = get_object_or_404(Menus, pk=pk)
    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def restaurant_with_menus(request, restaurant_id):
    # Get the restaurant or return a 404 if not found
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    
    # Get all categories for the restaurant
    categories = MenuCategory.objects.filter(menus__restaurant=restaurant).distinct()
    
    # Prepare the response data
    response_data = {
        'restaurant': RestaurantSerializer(restaurant).data,
        'categories': []
    }
    
    for category in categories:
        # Get all available menus for the current category and restaurant
        menus = Menus.objects.filter(restaurant=restaurant, category=category, is_available=True)
        category_data = {
            'category': MenuCategorySerializer(category).data,
            'menus': MenuSerializer(menus, many=True).data
        }
        response_data['categories'].append(category_data)
    
    return Response(response_data, status=status.HTTP_200_OK)
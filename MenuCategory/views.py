from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.middleware import AdminRoleMiddleware

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def menu_category_list(request):
    if request.method == 'GET':
        menu_categories = MenuCategory.objects.filter(user=request.user)
        serializer = MenuCategorySerializer(menu_categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MenuCategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save(user=request.user)
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def menu_category_detail(request, pk):
    menu_category = get_object_or_404(MenuCategory, pk=pk, user=request.user)
    if request.method == 'GET':
        serializer = MenuCategorySerializer(menu_category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenuCategorySerializer(menu_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

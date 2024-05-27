from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


class RestaurantList(APIView):
    """
    List all restaurants, or create a new restaurant.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        restaurants = Restaurant.objects.filter(user=request.user.id)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            restaurant = serializer.save(user=request.user)
            return Response(RestaurantSerializer(restaurant).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve_with_user_and_menus(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk, user=request.user)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class RestaurantDetail(APIView):
    """
    Retrieve, update or delete a restaurant instance.
    """

    permission_classes = [IsAuthenticated]
    def get_object(self, pk, user):
        return get_object_or_404(Restaurant, pk=pk, user=user)

    def get(self, request, pk):
        restaurant = self.get_object(pk, request.user)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk):
        restaurant = self.get_object(pk, request.user)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = self.get_object(pk, request.user)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

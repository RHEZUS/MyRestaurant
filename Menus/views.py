from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.http import Http404



from rest_framework.permissions import IsAuthenticated

class MenuListView(APIView):
    """
    List all menu items or create a new one.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetails(APIView):
    """
    Retrieve, update or delete a menu instance.
    """
    permission_classes = [IsAuthenticated]

    #def get_object(self, pk):
    #    try:
    #        return Menu.objects.get(pk=pk)
    #    except Menu.DoesNotExist:
    #        return Response(Http404)

    def get_object(self, pk, user):
        try:
            menu = Menu.objects.get(pk=pk)
            if menu.restaurant.user != user:
                #raise PermissionDenied("You do not have permission to modify this menu item.")
                raise Http404
            return menu
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def put(self, request, pk):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu = self.get_object(pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

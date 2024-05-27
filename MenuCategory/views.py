from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryList(APIView):
    """
    List all menu categories, or create a new menu category.
    """
    def get(self, request):
        menu_categories = MenuCategory.objects.all()
        serializer = MenuCategorySerializer(menu_categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuCategoryDetail(APIView):
    """
    Retrieve, update or delete a menu category instance.
    """
    def get_object(self, pk):
        try:
            return MenuCategory.objects.get(pk=pk)
        except MenuCategory.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            #raise Http404
    
    def get(self, request, pk):
        menu_category = self.get_object(pk)
        serializer = MenuCategorySerializer(menu_category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        menu_category = self.get_object(pk)
        serializer = MenuCategorySerializer(menu_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        menu_category = self.get_object(pk)
        menu_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



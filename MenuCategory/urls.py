from django.urls import path
from .views import MenuCategoryList, MenuCategoryDetail

urlpatterns = [
    path('categories/', MenuCategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', MenuCategoryDetail.as_view(), name='category-detail'),
]

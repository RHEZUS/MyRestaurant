from django.urls import path
from . import views

urlpatterns = [
    path('menu-categories/', views.menu_category_list, name='menu-category-list'),
    path('menu-categories/<int:pk>/', views.menu_category_detail, name='menu-category-detail'),
]

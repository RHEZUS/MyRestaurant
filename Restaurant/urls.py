from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant-list'),
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant-detail'),
]

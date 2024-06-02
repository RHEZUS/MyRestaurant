from . import views
from django.urls import path
urlpatterns =[
    path('menus/', views.menu_list, name='menu-list'),
    path('menus/<int:pk>/', views.menu_detail, name='menu-detail'),
    path('restaurant/<int:restaurant_id>/menus/', views.restaurant_with_menus, name='restaurant-with-menus'),
]

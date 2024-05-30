from . import views
from django.urls import path
urlpatterns =[
    path('menus/', views.menu_list, name='menu-list'),
    path('menus/<int:pk>/', views.menu_detail, name='menu-detail'),
]

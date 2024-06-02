from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('test-token/', views.test_token, name='test-token'),
]

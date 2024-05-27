from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Restaurant

class RestaurantTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password', email='test@example.com')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
    def test_create_restaurant(self):
        url = '/api/restaurants/'
        data = {
            'name': 'Test Restaurant',
            'description': 'Test Description',
            'location': 'Test Location'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Test Restaurant')
        
    def test_get_restaurants(self):
        url = '/api/restaurants/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_single_restaurant(self):
        restaurant = Restaurant.objects.create(owner=self.user, name='Test Restaurant', location='Test Location')
        url = f'/api/restaurants/{restaurant.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Restaurant')
        
    def test_update_restaurant(self):
        restaurant = Restaurant.objects.create(owner=self.user, name='Test Restaurant', location='Test Location')
        url = f'/api/restaurants/{restaurant.id}/'
        data = {'name': 'Updated Restaurant'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.get().name, 'Updated Restaurant')
        
    def test_delete_restaurant(self):
        restaurant = Restaurant.objects.create(owner=self.user, name='Test Restaurant', location='Test Location')
        url = f'/api/restaurants/{restaurant.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Restaurant.objects.count(), 0)

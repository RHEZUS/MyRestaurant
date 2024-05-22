# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = { "username": "Ludivin5", "password": "Pass1234", "email": "test5@gmail.com" }
        self.user = User.objects.create_user(username='existing_user', password='existing_password')

    def test_create_user(self):
        response = self.client.post('/api/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['username'], self.user_data['username'])
        # Check that the user object was created in the database
        self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming there's already one existing user
        self.assertEqual(response.data[0]['username'], self.user.username)

    def test_retrieve_user(self):
        response = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        new_username = 'updated_username'
        response = self.client.put(f'/api/users/{self.user.id}/', {'username': new_username, 'password': 'updated_password'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the user object was updated in the database
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.username, new_username)

    def test_delete_user(self):
        response = self.client.delete(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Check that the user object was deleted from the database
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

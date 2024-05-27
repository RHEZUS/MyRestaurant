from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import MenuCategory

class MenuCategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_category_data = { "name": "Test Menu Category", "slug": "test-menu-category", "desc": "This is a test menu category" }
        self.menu_category = MenuCategory.objects.create(name='existing_menu_category', slug='existing_slug', desc='existing_desc')
    
    def test_create_menu_category(self):
        response = self.client.post('/api/categories/', self.menu_category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['name'], self.menu_category_data['name'])
        # Check that the menu category object was created in the database
        self.assertTrue(MenuCategory.objects.filter(name=self.menu_category_data['name']).exists())

    def test_list_menu_categories(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming there's already one existing menu category
        self.assertEqual(response.data[0]['name'], self.menu_category.name)
    
    def test_retrieve_menu_category(self):
        response = self.client.get(f'/api/categories/{self.menu_category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.menu_category.name)
    
    def test_update_menu_category(self):
        new_name = 'updated_name2'
        slug = 'updated_slug'
        desc = 'description'
        response = self.client.put(f'/api/categories/{self.menu_category.id}/', {'name': new_name, 'slug':slug, 'desc': desc})
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the menu category object was updated in the database
        updated_menu_category = MenuCategory.objects.get(id=self.menu_category.id)
        self.assertEqual(updated_menu_category.name, new_name)
    
    def test_delete_menu_category(self):
        response = self.client.delete(f'/api/categories/{self.menu_category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Check that the menu category object was deleted from the database
        self.assertFalse(MenuCategory.objects.filter(id=self.menu_category.id).exists())


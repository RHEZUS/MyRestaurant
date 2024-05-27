from django.db import models
from Restaurant.models import Restaurant
from MenuCategory.models import MenuCategory


class Menus(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.name


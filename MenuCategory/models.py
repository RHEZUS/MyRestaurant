from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = models.TextField()

    def __str__(self):
        return self.name

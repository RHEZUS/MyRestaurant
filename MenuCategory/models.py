from django.db import models
from django.conf import settings

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    desc = models.TextField()
    #icon = models.TextField()

    def __str__(self):
        return self.name

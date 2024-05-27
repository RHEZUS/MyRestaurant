from django.db import models
from qr_code import qrcode
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File
from django.conf import settings

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    logo_url = models.URLField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
    desc = models.TextField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        qr_data = f'https://yourdomain.com/restaurants/{self.id}/menus/'
        qr_img = qrcode.make(qr_data)
        buffer = BytesIO()
        qr_img.save(buffer, format='PNG')
        self.qr_code.save(f'restaurant_{self.id}_qrcode.png', File(buffer), save=False)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.name

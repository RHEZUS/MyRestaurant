from django.db import models
#from qr_code import qrcode
import qr_code
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File
from django.conf import settings
import qr_code.qrcode
import qr_code.qrcode.maker
from qr_code.qrcode.utils import QRCodeOptions

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    logo_url = models.URLField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
    desc = models.TextField(null=True)

    #def save(self, *args, **kwargs):
    #    # Check if the instance already exists in the database
    #    if self.pk is not None:
    #        # Fetch the existing instance from the database
    #        old_instance = Restaurant.objects.get(pk=self.pk)
    #        # Delete the old QR code image if it exists
    #        if old_instance.qr_code:
    #            old_instance.qr_code.delete(save=False)
    #    
    #    # Save the new instance (and QR code image)
    #    super().save(*args, **kwargs)
    #    
    #    # Generate and save the new QR code image
    #    qr_data = f'https://yourdomain.com/restaurants/{self.id}/menus/'
    #    qr_options = QRCodeOptions()
    #    qr_img = qr_code.qrcode.maker.make_qr_code_image(qr_data, qr_code_options=qr_options)
    #    buffer = BytesIO()
    #    buffer.write(qr_img)
    #    self.qr_code.save(f'restaurant_{self.id}_qrcode.png', File(buffer), save=False)
    #    super().save(*args, **kwargs)
    #    #self.save(*args, **kwargs)

    

    def __str__(self):
        return self.name

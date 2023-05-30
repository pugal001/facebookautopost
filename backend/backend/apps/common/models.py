from django.db import models

# Create your models here.

class Templates(models.Model):
    message = models.CharField(max_length=2000)
    template_image = models.FileField(upload_to='template_images')

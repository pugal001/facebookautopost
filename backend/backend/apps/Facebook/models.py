from django.db import models

# Create your models here.

class Details(models.Model):
    facebook_id = models.CharField(max_length=2000, null=True, blank=True)
    name = models.CharField(max_length=2000, null=True, blank=True)
    email = models.EmailField(max_length=2000, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    message = models.FileField(upload_to='template_images')
    API_key = models.CharField(max_length=2000, null=True, blank=True)

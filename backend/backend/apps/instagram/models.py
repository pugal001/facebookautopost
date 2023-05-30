from django.db import models

# Create your models here.

class InstaUser(models.Model):
    insta_user_name = models.CharField(max_length=2000, null=True, blank=True, default=None)
    insta_user_id = models.IntegerField(null=True, blank=True, default=None)
    number_of_posts = models.IntegerField(null=True, blank=True, default=None)
    followers_count = models.IntegerField(null=True, blank=True, default=None)
    following_count = models.IntegerField(null=True, blank=True, default=None)
    biography = models.CharField(max_length=2000, null=True, blank=True, default=None)
    external_url = models.CharField(max_length=2000, null=True, blank=True, default=None)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, null=True, blank=True, default=None)
    image = models.FileField(upload_to='intagram_images',  null=True, blank=True, default=None)
    password = models.CharField(max_length=2000, null=True, blank=True, default=None)

    def __str__(self):
        return self.insta_user_name
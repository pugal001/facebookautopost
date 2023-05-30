
#from accounts.emails import ClaimAcceptedEmailTemplate , ClaimPendingEmailTemplate
from django.db import models
import datetime
import re
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)




def create_username(email: str) -> str:
    split_email = email.split('@')
    if len(split_email) < 2:
        raise ValueError('Cannot get username from email')
    username = split_email[0]
    users_username_count = User.objects.filter(username=username).count()
    username = f'@{username}' if users_username_count < 1 else f'@{username}{users_username_count}'
    return username


def user_picture(instance, filename):
    return f'user_image/{datetime.datetime.now()}_{filename}'


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            username = create_username(email)

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not username:
            username = create_username(email)
        user = self.create_user(
            email,
            username=username,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_verified = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255, default="Aqua")
    last_name = models.CharField(max_length=255, default="User")
    phone_no = models.CharField(max_length=20, blank=True,)
    company_name = models.CharField(max_length=200, default='', blank=True)
    sic_gst_code = models.CharField(max_length=200, default='', blank=True)
    pan_no = models.CharField(max_length=200, default='', blank=True)
    address_one = models.TextField(default='', blank=True)
    address_two = models.TextField(default='', blank=True)
    pincode = models.IntegerField(default=0, blank=True)
    website = models.URLField(max_length=200, default='', blank=True)
    username = models.CharField(
        'username', max_length=30, unique=False, default="",
        validators=[
            validators.RegexValidator(
                re.compile(r'^[\w.@+-]+$'), 'put valid username', 'username is invalid')
        ]
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_terms_accepted = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_no']

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_verified_user(self):
        "Is the user a verified user?"
        # Simplest possible answer: All admins are staff but not normal user
        return self.is_verified

    def save(self, *args, **kwargs):
        if self.is_verified == False:        
            # ClaimPendingEmailTemplate.send_email(
            #     subject="Success! Your Request profile verification has been received.",
            #     email_receivers=[self.email],
            #     instance=self,
            # )
            print(self.is_verified,'verified pending')
            super(User, self).save(*args, **kwargs)
        elif self.is_verified == True:        
            # ClaimAcceptedEmailTemplate.send_email(
            #     subject="Success! Your Request profile verification has been received.",
            #     email_receivers=[self.email],
            #     instance=self,
            # )
            print(self.is_verified,'verification completed')
            super(User, self).save(*args, **kwargs)
            
 

class Image(models.Model):

    image_name = models.CharField(max_length=400, null=True)
    image = models.FileField(upload_to='user_images', null=True)
    images = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_images', default=None, null=True)

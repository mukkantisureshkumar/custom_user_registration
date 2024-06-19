from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email is not provided')
        ne=self.normalize_email(email)
        uo=self.model(email=ne,first_name=first_name,last_name=last_name)
        uo.set_password(password)
        uo.save()
        return uo
    def create_superuser(self,email,first_name,last_name,password):
        uo=self.create_user(email,first_name,last_name,password)
        uo.is_staff=True
        uo.is_superuser=True
        uo.save()

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    objects=UserProfileManager()
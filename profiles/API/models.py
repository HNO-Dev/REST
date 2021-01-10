from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.
# 1)subs custom user model

class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        """create a new user profile object"""
         
        if not email:
            raise ValueError("Users need a email address")

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True

        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"rep a user profile in our system"""

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
 
    def get_full_name(self):
        """üsers full name"""
        return self.name

    def get_short_name(self):
        return self.name

    
    def __str__(self):
        return self.name 
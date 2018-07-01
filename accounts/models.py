from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email =models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=True)
    date_joined =models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']
    def __str__(self):
        return '%s' % self.username
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
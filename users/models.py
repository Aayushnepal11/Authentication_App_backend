from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

GENDER = (
    ('male', "Male"),
    ('female', "Female"),
    ('other', "Other"),
)

class User(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(_("email_address"), unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=150, choices=GENDER, default='male')
    username = None

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



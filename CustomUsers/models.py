from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom User Model"""

    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    password = models.CharField(max_length=150)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
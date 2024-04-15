from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django_project import settings
from twits.models import Twit

# Benjamin Heerlyn
# CIS218
# 4/15/2024

class CustomUser(AbstractUser):
    """Custom User Model"""
    date_of_birth = models.DateField(null=True, blank=True)
    

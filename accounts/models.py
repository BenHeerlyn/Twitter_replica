from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django_project import settings

class CustomUser(AbstractUser):
    """Custom User Model"""
    date_of_birth = models.DateField(null=True, blank=True)

class Private(models.Model):
    """A model that allows a user to update their private profile to their liking"""
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse("private_profile")

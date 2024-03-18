from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom User Model"""

    date_of_birth = models.DateField(null=True, blank=True)
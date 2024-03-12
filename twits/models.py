from django.db import models
# Register your models here.

class Twits(models.Model):
    """Twits users can create"""

    body = models.TextField()
    # image = 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
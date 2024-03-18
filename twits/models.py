from django.db import models
from django.urls import reverse
from django.conf import settings
# Register your models here.

class Twit(models.Model):
    """Twits users can create"""

    body = models.TextField()
    # image = 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    def __str__(self):
        """ String method"""
        return self.body
    
    def get_absolute_url(self):
        return reverse("twit_detail", kwargs={"pk": self.pk})
    
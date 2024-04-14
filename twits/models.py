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
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_twits",
        blank=True,
    )
    def __str__(self):
        """ String method"""
        return self.body
    
    def get_absolute_url(self):
        return reverse("twit_detail", kwargs={"pk": self.pk})
    
    def get_like_url(self):
        """Get the like url based on the pk of the twit"""
        return reverse("twit_like", kwargs={"pk": self.pk})
        
    
class Comment(models.Model):
    """Comment Class"""

    comment = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    twit = models.ForeignKey(
        Twit,
        on_delete = models.CASCADE,
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """String Method"""
        return self.comment
    
    def get_absolute_url(self):
        return reverse("twit_list")
    
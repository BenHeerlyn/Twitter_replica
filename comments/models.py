from django.db import models
from twits.models import Twits
# Create your models here.

class Comment(models.Model):
    """Comment Model"""
    twit = models.ForeignKey(
        Twits,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE,
        related_name="comments",
    )

    comment = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

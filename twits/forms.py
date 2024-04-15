from django import forms

from .models import Comment

# Benjamin Heerlyn
# CIS218
# 4/15/2024

class CommentForm(forms.ModelForm):
    """Comment form class"""
    class Meta:
        model = Comment
        fields = ("comment",)
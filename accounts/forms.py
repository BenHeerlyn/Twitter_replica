from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# Benjamin Heerlyn
# CIS218
# 4/15/2024

class CustomUserCreateForm(UserCreationForm):
    """Custom User Create Form"""
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
        )
    
class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""
    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        )
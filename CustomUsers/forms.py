from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreateForm(UserCreationForm):
    """Custom User Create Form"""
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "date_of_birth",
        )
    
class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""
    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "date_of_birth",
        )
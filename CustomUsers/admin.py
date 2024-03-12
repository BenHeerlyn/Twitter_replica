from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreateForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Custom User Admin to register the custom user model in the admin"""

    add_form = CustomUserCreateForm

    form = CustomUserChangeForm

    model = CustomUser
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_staff",
    ]

    fieldset = UserAdmin.fieldsets + (
        (None, 
        {"fields": (
            "first_name", 
            "last_name",
            "date_of_birth",
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,
        {"fields": (
            "first_name",
            "last_name",
            "date_of_birth",
            )
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)
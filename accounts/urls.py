from django.urls import path
from .views import SignUpView, PrivateProfileView, PublicProfileView

# Benjamin Heerlyn
# CIS218
# 4/15/2024

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("private_profile/<int:pk>/", PrivateProfileView.as_view(), name="private_profile"),
    path("public_profile/<int:pk>/", PublicProfileView.as_view(), name="public_profile"),
]

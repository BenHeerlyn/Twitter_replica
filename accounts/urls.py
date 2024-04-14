from django.urls import path
from .views import SignUpView, PrivateProfileView
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("private_profile/<int:pk>/", PrivateProfileView.as_view(), name="private_profile"),
]

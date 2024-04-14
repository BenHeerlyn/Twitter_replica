from django.urls import path
from .views import SignUpView, PrivateProfileView
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/private_profile/", PrivateProfileView.as_view(), name="private_profile"),
]

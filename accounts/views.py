from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreateForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import CustomUser

# Benjamin Heerlyn
# CIS218
# 4/15/2024

class SignUpView(CreateView):
    """SignUp view"""
    form_class = CustomUserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class PrivateProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Private Profile View"""
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("twit_list")
    template_name = "registration/private_profile.html"

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

class PublicProfileView(DetailView):
    """A profile that displays a user's every post, but also some info about them"""
    model = CustomUser
    template_name = "registration/public_profile.html"

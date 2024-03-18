from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """Home Page List View"""
    template_name = "home.html"
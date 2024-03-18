from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Twit
from django.urls import reverse_lazy

# Create your views here.

class TwitListView(ListView):
    """Twit List View"""
    model = Twit
    template_name = "twit_list.html"

class TwitDetailView(DetailView):
    """Twit Detail View"""
    model = Twit
    template_name = "twit_detail.html"

class TwitUpdateView(UpdateView):
    """Twit Create View"""
    model = Twit
    fields = (
        "body",
        "date_of_birth",
    )
    template_name = "twit_edit.html"

class TwitDeleteView(DeleteView):
    """Twit Delete View"""
    model = Twit
    template_name = "twit_delete.html"
    success_url = reverse_lazy("twit_list")
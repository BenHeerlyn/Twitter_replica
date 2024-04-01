from .views import (
    TwitDeleteView,
    TwitDetailView,
    TwitListView,
    TwitUpdateView,
    TwitCreateView,
    TwitLikeView,
    )
from django.urls import path

urlpatterns = [
    path("<int:pk>/", TwitDetailView.as_view(), name="twit_detail"),
    path("<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("<int:pk>/like/", TwitLikeView.as_view(), name="twit_like"),
    path("add/", TwitCreateView.as_view(), name="twit_add"),
    path("", TwitListView.as_view(), name="twit_list"),
]

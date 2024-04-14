from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from .models import Twit, Comment
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.http import JsonResponse
from .forms import CommentForm

class TwitListView(LoginRequiredMixin, ListView):
    """Twit List View"""
    model = Twit
    template_name = "twit_list.html"

class TwitDetailView(LoginRequiredMixin, View):
    """Twit Detail View"""
    def get(self,request, *args, **kwargs):
        """Doing a request"""
        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """Doing Post request"""
        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)

class CommentGetView(DetailView):
    """Comment Get View"""
    model = Twit
    template_name = "twit_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPostView(SingleObjectMixin, FormView):
    """Comment Post View"""
    model = Twit
    template_name = "twit_detail.html"
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        """Create new comment when form is valid"""
        # Get the comment instance by saving the form, but set commit to false
        # as we don't want the form to actually save to the database yet
        comment = form.save(commit=False)

        # Attach the twit to the new comment.
        comment.twit = self.object

        # Attatch the user to the post user
        comment.author = self.request.user

        # save the comment instance to the database
        comment.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        twit = self.get_object()
        return reverse("twit_detail", kwargs={"pk": twit.pk})
    
class TwitUpdateView(LoginRequiredMixin, UpdateView):
    """Twit Create View"""
    model = Twit
    fields = (
        "body",
    )
    template_name = "twit_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Twit Delete View"""
    model = Twit
    template_name = "twit_delete.html"
    success_url = reverse_lazy("twit_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TwitCreateView(LoginRequiredMixin, CreateView):
    """Twit Create View"""
    model = Twit
    template_name = "twit_add.html"
    fields = (
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TwitLikeView(LoginRequiredMixin, View):
    """Twit Like View"""

    def get(self, request, *args, **kwargs):
        """Get Request"""

        # get the data from the GET request
        twit_id = request.GET.get("twit_id", None)
        twit_action = request.GET.get("twit_action", None)
        
        print(twit_id)
        print(twit_action)

        twit = Twit.objects.get(id=twit_id)
        if twit_action == "like":
            twit.likes.add(request.user)
        else:
            twit.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True,
            }
        )

# class CommentCreateView(LoginRequiredMixin, CreateView):
#     """Allows a User to create a comment under a Twit of their choosing"""

#     model = Comment
#     template_name = "comment_create.html"
#     fields = (
#         "comment",
#     )

#     def form_valid(self, form):
#         """Create new comment when form is valid"""
#         # Get the comment instance by saving the form, but set commit to false
#         # as we don't want the form to actually save to the database yet
#         comment = form.save(commit=False)

#         # Attatch the user to the post user
#         comment.author = self.request.user

#         # save the comment instance to the database
#         comment.save()

#         return super().form_valid(form)
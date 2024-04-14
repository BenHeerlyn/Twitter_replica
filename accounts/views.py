from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, View
from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import Private

class SignUpView(CreateView):
    """SignUp view"""
    form_class = CustomUserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class PrivateProfileView(View):
    """Private Profile View"""

    def get(self,request, *args, **kwargs):
        """Doing a request"""
        view = PrivateGetView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """Doing Post request"""
        view = PrivatePostView.as_view()
        return view(request, *args, **kwargs)

class PrivatePostView(FormView):
    """Private Profile View"""
    model =Private
    template_name = "private_profile.html"
    form_class = CustomUserChangeForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        """Create new comment when form is valid"""
        # Get the comment instance by saving the form, but set commit to false
        # as we don't want the form to actually save to the database yet
        private = form.save(commit=False)

        private.author = self.object

        # save the comment instance to the database
        private.save()

        return super().form_valid(form)
    
class PrivateGetView(DetailView):
    """Private Profile View"""
    model = Private
    template_name = "private_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CustomUserChangeForm()
        return context
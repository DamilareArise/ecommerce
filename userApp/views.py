from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'
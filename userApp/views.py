from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm
from django.contrib.auth.models import User


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'
    
    
# def handleProfile(request, user_id):
#     user = get_object_or_404(User, id=user_id)
    
#     if request.method == 'POST':
#         pass
#     else:
#         profile_form = ProfileForm(instance=user)
#         return render(request, template_name='profile.html',  context={'profile_form': profile_form})
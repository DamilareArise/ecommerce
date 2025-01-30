from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm, ProfileForm, userForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from ecommerce.productApp.decorators import staff_required


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'
    
@login_required
def viewProfile(request, userId):
    user = get_object_or_404(User, id=userId)
    profile = get_object_or_404(Profile, user_id=userId)
    
    return render(request, template_name='viewProfile.html', context={'user': user, 'profile': profile})
    
@login_required    
def editProfile(request, userId):
    user = get_object_or_404(User, id=userId)
    profile = get_object_or_404(Profile, user_id=userId)
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = userForm(request.POST, instance=user)
        
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            
            messages.success(request, "Profile details updated.")
            
            return redirect('view-profile', userId=userId)
        else:
            print(profile_form.errors)
            print(user_form.errors)
            
            messages.error(request, "Error updating profile details.")
        
            return render(request, template_name='editProfile.html',  context={'profile_form': profile_form, 'user_form': user_form})
            
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = userForm(instance=user)
        return render(request, template_name='editProfile.html',  context={'profile_form': profile_form, 'user_form': user_form})
    
    
@staff_required
@login_required
def view_user_staff(request, action):
    if action == 'staff':
        users = User.objects.filter(is_staff=True)
    else:
        users = User.objects.filter(is_staff=False)
        
    return render(request, template_name='viewUsers.html', context={'users': users, 'action': action})

@staff_required
@login_required
def makeStaff(request, userId):
    user = get_object_or_404(User, id=userId)
    if user.is_staff:
        user.is_staff = False
        messages.success(request, "User is no longer a staff.")
        
    else:
        user.is_staff = True
        messages.success(request, "User is now a staff.")
        
    user.save()
    
    return redirect('view-user', action='staff')


@staff_required
@login_required
def deactivateUser(request, userId):
    user = get_object_or_404(User, id=userId)
    if user.is_active:
        user.is_active = False
        messages.success(request, "User account is now deactivated.")
        
    else:
        user.is_active = True
        messages.success(request, "User account is now activated.")
        
    user.save()
    
    return redirect('view-user', action='staff')
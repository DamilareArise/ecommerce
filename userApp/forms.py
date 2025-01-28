from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from .getCountries import get_countries

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        
        
class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
        }
        
class ProfileForm(forms.ModelForm):

    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 30, 'class': 'form-control mb-2'}), 
        required=False
        )
    profile_picture = forms.ImageField(
        required=False, 
        widget=forms.FileInput(attrs={'class': 'form-control mb-2'})
        )
    country = forms.ChoiceField(
        choices=get_countries(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control mb-2'})
        )
    
    class Meta:
        model = Profile
        fields = [
            'bio',
            'profile_picture',
            'date_of_birth',
            'country'
        ]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control mb-2'}),
            'date_of_birth': forms.NumberInput(attrs={'type':'date', 'class': 'form-control mb-2'}),
        }
from .views import SignUpView, handleProfile
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:user_id>/', handleProfile, name='profile'),
]

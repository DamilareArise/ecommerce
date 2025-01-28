from .views import SignUpView, editProfile, viewProfile
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('view-profile/<int:userId>/', viewProfile, name='view-profile'),
    path('edit-profile/<int:userId>/', editProfile, name='edit-profile')
]

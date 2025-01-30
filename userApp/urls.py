from .views import *
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('view-profile/<int:userId>/', viewProfile, name='view-profile'),
    path('edit-profile/<int:userId>/', editProfile, name='edit-profile'),
    path('view-user/<str:action>/', view_user_staff, name='view-user' ),
    path('make-staff/<int:userId>/', makeStaff, name='make-staff'),
    path('deactivate-user/<int:userId>/', deactivateUser, name='deactivate-user'),
]

from .views import SignUpView, Profile, UpdateProfileView
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:username>/', Profile.as_view(), name='profile'),
    path('update', UpdateProfileView.as_view(), name='update'),
]

from .views import SignUpView, Profile, UpdateProfileView, AddRemoveSavedView, SavedView, RecentlyViewed
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:username>/', Profile.as_view(), name='profile'),
    path('update', UpdateProfileView.as_view(), name='update'),
    path('addremovesaved/<int:product_id>/', AddRemoveSavedView.as_view(), name='addremovesaved'),
    path('saveds/', SavedView.as_view(), name='saveds'),
    path('recently/', RecentlyViewed.as_view(), name='recently')
]

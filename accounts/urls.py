from django.urls import path
from .views import signup, profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
]
from django.urls import path
from .views import signup, profile, logout_confirm, custom_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', custom_logout, name='logout'),
    path('logout/confirm/', logout_confirm, name='logout_confirm'),
]

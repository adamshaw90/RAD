from django.urls import path
from .views import (
    profile, logout_confirm, custom_logout, delete_account,
    confirm_delete_account, edit_profile, CustomSignupView
)

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('profile/', profile, name='profile'),
    path('logout/', custom_logout, name='logout'),
    path('logout/confirm/', logout_confirm, name='logout_confirm'),
    path('delete/confirm/', delete_account, name='delete_account'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', confirm_delete_account,
         name='confirm_delete_account'),
]

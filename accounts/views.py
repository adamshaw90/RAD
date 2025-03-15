from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm, ProfileUpdateForm
from django.contrib.auth import logout, login
from django.contrib import messages
from allauth.account.views import SignupView


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'account/profile.html', {'form': form})


def logout_confirm(request):
    return render(request, 'account/logout_confirm.html')


def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    request.session.flush()
    return redirect('home')


@login_required
def confirm_delete_account(request):
    return render(request, 'account/confirm_delete.html')


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, "Your account has been successfully deleted.")
        return redirect('home')

    return redirect('confirm_delete_account')


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'account/edit_profile.html', {'form': form})


class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)
        messages.info(self.request, "Please check your email and confirm your account before logging in.")
        return redirect("/accounts/confirm-email/")

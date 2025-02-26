from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Creates the user
            # Optionally, log the user in or display a success message
            return redirect('home')  # Or wherever you want to redirect after signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Refresh the profile page or redirect as needed
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})


def logout_confirm(request):
    return render(request, 'accounts/logout_confirm.html')


def custom_logout(request):
    messages.success(request, "You have been logged out successfully.")  # Add message
    logout(request)  # Manually log out the user
    request.session.flush()  # Clear the session completely
    return redirect('home')  # Redirect to homepage

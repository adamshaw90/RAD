from django.shortcuts import render, redirect
from shop.models import Product
from .forms import ContactForm
from .models import ContactMessage
from django.contrib import messages


def home(request):
    favourite_products = Product.objects.filter(is_favourite=True)
    return render(request, 'core/home.html',
                  {'favourite_products': favourite_products})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                enquiry=form.cleaned_data['enquiry']
            )
            messages.success(request, "Your message has been received, we will respond to you shortly!")
            return redirect('contact')

    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def wholesale(request):
    return render(request, 'core/wholesale.html')

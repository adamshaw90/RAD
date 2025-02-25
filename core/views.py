from django.shortcuts import render, redirect
from shop.models import Product
from .forms import ContactForm


def home(request):
    favourite_products = Product.objects.filter(is_favourite=True)
    return render(request, 'core/home.html', {'favourite_products': favourite_products})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here:
            # For example, send an email, save the enquiry in the database, etc.
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # enquiry = form.cleaned_data['enquiry']
            # (Do something with the data)

            # Optionally, redirect to a thank-you page or render a success message
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})



def wholesale(request):
    return render(request, 'core/wholesale.html')

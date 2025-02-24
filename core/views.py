from django.shortcuts import render
from shop.models import Product


def home(request):
    favourite_products = Product.objects.filter(is_favourite=True)
    return render(request, 'core/home.html', {'favourite_products': favourite_products})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def wholesale(request):
    return render(request, 'core/wholesale.html')

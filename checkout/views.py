from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from shop.models import Product
from decimal import Decimal


def checkout(request):
    cart = request.session.get('cart', {})  # Ensure consistency with other views
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('shop'))  # Ensure redirect is to the correct view

    cart_items = []
    total = Decimal('0.00')

    for product_id, item in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * Decimal(item['quantity'])

        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'subtotal': subtotal,
        })
        total += subtotal

    delivery = Decimal('5.00')  # Set a fixed delivery fee or calculate dynamically
    grand_total = total + delivery

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
        'product_count': len(cart_items),
    }

    return render(request, 'checkout/checkout.html', context)

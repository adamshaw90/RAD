from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from shop.models import Product
from decimal import Decimal
from shop.context_processors import cart_total
import stripe
from django.conf import settings


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})  # Ensure consistency with other views
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('shop'))  # Ensure redirect is to the correct view

    current_cart = cart_total(request)
    total = current_cart['cart_total']  # Make sure this key exists in the context processor
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    # ✅ Corrected placement of `cart_items` and `total`
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

    # ✅ Create Stripe Payment Intent AFTER calculations
    intent = stripe.PaymentIntent.create(
        amount=int(grand_total * 100),  # Convert to cents
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
        'product_count': len(cart_items),
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,  # ✅ Get actual client secret
    }

    return render(request, 'checkout/checkout.html', context)

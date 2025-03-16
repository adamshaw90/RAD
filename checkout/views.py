from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from shop.models import Product
from decimal import Decimal
from shop.context_processors import cart_total
import stripe
import json
from django.conf import settings
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ Handle checkout process """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})  # Ensure consistency with other views
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('shop'))  # Redirect to shop if cart is empty

    # Calculate totals
    total = Decimal('0.00')
    cart_items = []

    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * Decimal(item['quantity'])

        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'subtotal': subtotal,
        })
        total += subtotal

    delivery = Decimal('5.00')  # Fixed delivery fee
    grand_total = total + delivery

    stripe_total = round(grand_total * 100)  # Convert to cents
    stripe.api_key = stripe_secret_key

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data['quantity'],
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products in your cart wasn't found. Please try again.")
                    order.delete()
                    return redirect(reverse('cart'))  # Redirect back to cart

            request.session['save_info'] = 'save-info' in request.POST
            request.session['cart'] = {}  # Clear cart after successful checkout
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double-check your information.')

    else:
        # Create Stripe Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. '
                                      'Did you forget to set it in your environment?')

        context = {
            'order_form': order_form,
            'cart_items': cart_items,
            'total': total,
            'delivery': delivery,
            'grand_total': grand_total,
            'product_count': len(cart_items),
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """ Handle successful checkouts """
    order = get_object_or_404(Order, order_number=order_number)
    save_info = request.session.get('save_info')

    # Send confirmation email
    subject = f"Order Confirmation - {order_number}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.email]

    # Render email template
    context = {'order': order}
    html_message = render_to_string('checkout/order_confirmation_email.html', context)
    plain_message = strip_tags(html_message)

    try:
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
        messages.success(request, f'Order successfully processed! A confirmation email has been sent to {order.email}.')
    except Exception as e:
        messages.error(request, 'Your order was placed, but we could not send a confirmation email.')

    # Clear cart
    if 'cart' in request.session:
        del request.session['cart']

    return render(request, 'checkout/checkout_success.html', {'order': order})

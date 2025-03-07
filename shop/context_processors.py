from .models import Product
from decimal import Decimal
from django.conf import settings


def cart_total(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = Decimal('0.00')

    for product_id, item in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            
            # Ensure `item` is a dictionary before accessing keys
            if isinstance(item, dict) and 'price' in item and 'quantity' in item:
                subtotal = Decimal(item['price']) * item['quantity']
                cart_items.append({
                    'product': product,
                    'quantity': item['quantity'],
                    'subtotal': subtotal,
                    'image': product.image.url if product.image else '/static/images/placeholder.jpg'
                })
                total += subtotal
            else:
                # If item is an integer (corrupt data), reset it
                cart[product_id] = {
                    'name': product.name,
                    'price': float(product.price),
                    'quantity': 1  # Default quantity
                }
        except Product.DoesNotExist:
            continue

    # Save back corrected cart session to avoid future errors
    request.session['cart'] = cart

    return {'cart_total': round(total, 2), 'cart_items': cart_items}


def media_url(request):
    return {'MEDIA_URL': settings.MEDIA_URL}

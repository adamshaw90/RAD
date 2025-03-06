from .models import Product
from decimal import Decimal


def cart_total(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = Decimal('0.00')

    for product_id, item in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            subtotal = Decimal(item['price']) * item['quantity']
            cart_items.append({
                'product': product,
                'quantity': item['quantity'],
                'subtotal': subtotal,
            })
            total += subtotal
        except Product.DoesNotExist:
            continue

    return {'cart_total': round(total, 2), 'cart_items': cart_items}

from .models import Product
from decimal import Decimal
from django.conf import settings


def cart_total(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')

    for product_id, item in cart.items():
        try:
            # ✅ Ensure product_id is an integer
            if not product_id.isdigit():
                continue

            product = Product.objects.get(id=int(product_id))  # ✅ Convert to integer

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
                cart[product_id] = {
                    'name': product.name,
                    'price': float(product.price),
                    'quantity': 1
                }

        except Product.DoesNotExist:
            print(f"⚠️ Product ID {product_id} not found!")
            continue
        except ValueError as e:
            print(f"❌ ValueError: {e} for key {product_id}")
            continue

    request.session['cart'] = cart  # Save fixed cart
    return {'cart_total': round(total, 2), 'cart_items': cart_items}

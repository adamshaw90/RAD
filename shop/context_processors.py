from decimal import Decimal


def cart_total(request):
    cart = request.session.get('cart', {})

    total = sum(
        Decimal(item['price']) * item['quantity']
        for item in cart.values() if isinstance(item, dict)  # ✅ Ensure item is a dictionary
    )

    return {'cart_total': round(total, 2)}

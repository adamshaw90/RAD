from .models import Product


def cart_total(request):
    cart = request.session.get('cart', {})
    total_price = sum(Product.objects.get(id=pid).price * quantity for pid, quantity in cart.items())
    return {'cart_total': round(total_price, 2)}

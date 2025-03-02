from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Product, Order, OrderItem, Review
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ReviewForm
from django.contrib import messages
from django.urls import reverse
from decimal import Decimal


def shop(request):
    """ Displays the shop page with search and filters """
    products = Product.objects.all()

    # Handle search queries
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Handle price sorting
    price_order = request.GET.get('price_order')
    if price_order == 'low':
        products = products.order_by('price')
    elif price_order == 'high':
        products = products.order_by('-price')

    # Handle favourite products filter
    favourite_filter = request.GET.get('favourite_filter')
    if favourite_filter == 'favourites':
        products = products.filter(is_favourite=True)

    return render(request, 'shop/shop.html', {
        'products': products,
        'query': query,
        'price_order': price_order,
        'favourite_filter': favourite_filter,
    })


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all().order_by('-created_at')
        context['form'] = ReviewForm()
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop')


@login_required
def cart_view(request):
    """ Displays the shopping cart with accurate total calculations. """
    cart = request.session.get('cart', {})

    cart_items = []
    total_price = Decimal('0.00')

    for product_id, item in cart.items():
        product = get_object_or_404(Product, pk=product_id)

        # Ensure quantity is correctly extracted from the stored dictionary
        quantity = item.get('quantity', 1)
        subtotal = product.price * Decimal(quantity)

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': round(subtotal, 2),  # ✅ Ensures proper decimal formatting
            'price': round(product.price, 2),
        })

        total_price += subtotal

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total_price': round(total_price, 2)  # ✅ Rounds final total price
    })


# ✅ Add product to cart
def add_to_cart(request, product_id):
    """ Adds a product to the cart with correct quantity handling. """
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})

    # Get quantity from form (default to 1)
    quantity = int(request.POST.get('quantity', 1))
    product_key = str(product_id)  # Ensure product_id is stored as a string key

    if product_key in cart:
        cart[product_key]['quantity'] += quantity  # ✅ Correctly increment quantity
    else:
        cart[product_key] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': quantity
        }

    request.session['cart'] = cart  # ✅ Save the cart
    messages.success(request, f"{quantity}x {product.name} added to cart.")
    return redirect('cart')


# ✅ Remove product from cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]  # Remove item
        request.session['cart'] = cart
        messages.success(request, "Item removed from cart.")

    return redirect('cart')


def update_cart(request, product_id):
    """ Updates the cart when the user changes quantity in cart page. """
    if request.method == "POST":
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get("quantity", 1))

        product_key = str(product_id)

        if product_key in cart:
            if quantity > 0:
                cart[product_key]['quantity'] = quantity  # ✅ Correctly update quantity
            else:
                del cart[product_key]  # ✅ Remove item if quantity is 0

        request.session['cart'] = cart  # ✅ Save cart session
        messages.success(request, "Cart updated successfully.")
    
    return redirect('cart')


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('shop')

    line_items = []

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(product.price * 100),
                'product_data': {
                    'name': product.name,
                },
            },
            'quantity': quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/shop/'),
        cancel_url=request.build_absolute_uri('/shop/cart/'),
    )
    return redirect(session.url, code=303)


# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
#     endpoint_secret = os.environ.get('STRIPE_WEBHOOK_SECRET', 'your_webhook_secret')
#     try:
#         event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
#     except (ValueError, stripe.error.SignatureVerificationError):
#         return HttpResponse(status=400)

#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']
#         # Process the order: create Order and OrderItems, mark as paid, etc.
#     return HttpResponse(status=200)


@login_required
def submit_review(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect(reverse('product_detail', kwargs={'pk': product.pk}))

    messages.error(request, "There was an issue submitting your review.")
    return redirect(reverse('product_detail', kwargs={'pk': product.pk}))


@login_required
def edit_review(request, product_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk, user=request.user)
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated!")
            return redirect(reverse('product_detail', kwargs={'pk': product.pk}))

    else:
        form = ReviewForm(instance=review)

    return render(request, 'shop/edit_review.html', {'form': form, 'product': product})


@login_required
def delete_review(request, product_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk, user=request.user)
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == "POST":
        review.delete()
        messages.success(request, "Your review has been deleted!")
        return redirect(reverse('product_detail', kwargs={'pk': product.pk}))

    return render(request, 'shop/delete_review.html', {'review': review, 'product': product})


def cart_total_api(request):
    """ Returns the total cart price for AJAX updates. """
    cart = request.session.get('cart', {})
    total_price = Decimal('0.00')

    for product_id, item in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        quantity = item.get('quantity', 1)
        total_price += product.price * Decimal(quantity)

    return JsonResponse({'cart_total': round(total_price, 2)})
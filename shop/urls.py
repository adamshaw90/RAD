from django.urls import path
from . import views
from .views import (
    shop, ProductDetailView, ProductCreateView, ProductUpdateView,
    ProductDeleteView, checkout, submit_review, cart_view, add_to_cart,
    remove_from_cart
)

urlpatterns = [
    path('', shop, name='shop'),
    path('product/<int:pk>/',
         ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/',
         ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product_delete'),
    path('checkout/', checkout, name='checkout'),
    path('product/<int:pk>/review/', submit_review, name='submit_review'),
    path('product/<int:product_pk>/review/<int:review_pk>/edit/',
         views.edit_review, name='edit_review'),
    path('product/<int:product_pk>/review/<int:review_pk>/delete/',
         views.delete_review, name='delete_review'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/',
         remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/',
         views.update_cart, name='update_cart'),
    path('cart/total/', views.cart_total_api, name='cart_total_api'),
]

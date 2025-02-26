from django.urls import path
from .views import (
    shop, ProductDetailView, ProductCreateView, ProductUpdateView,
    ProductDeleteView, cart, checkout, submit_review
)

urlpatterns = [
    path('', shop, name='shop'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('product/<int:pk>/review/', submit_review, name='submit_review'),
]

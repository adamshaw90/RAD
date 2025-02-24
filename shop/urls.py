from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    # path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
]

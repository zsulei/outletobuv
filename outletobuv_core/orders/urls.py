# urls.py

from django.urls import path
from .views import CartView, AddToCartView

app_name = 'orders'
urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
]

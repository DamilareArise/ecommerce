from .views import add_to_cart
from django.urls import path

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
]

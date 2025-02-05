from .views import add_to_cart, viewCart, reduceQuantity
from django.urls import path

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('view-cart/', viewCart, name='view-cart'),
    path('reduce-quantity/<int:product_id>/', reduceQuantity, name='reduce-quantity'),
    
]

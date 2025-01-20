from django.urls import path
from .views import addProduct, home, viewProduct, deleteProduct, editProduct

urlpatterns = [
    path('add-product/', addProduct, name='add-product'),
    path('view-product/<int:product_id>/', viewProduct, name='view-product'),
    path('delete-product/<int:product_id>/', deleteProduct, name='delete-product'),
    path('edit-product/<int:product_id>/', editProduct, name='edit-product')
]

from django.urls import path
from .views import *

urlpatterns = [
    path('add-product/', addProduct, name='add-product'),
    path('view-product/<int:product_id>/', viewProduct, name='view-product'),
    path('delete-product/<int:product_id>/', deleteProduct, name='delete-product'),
    path('edit-product/<int:product_id>/', editProduct, name='edit-product'),
    path('view-all-products/', viewAllProducts, name='view-all-products'),
    path('approve-reject-product/<int:product_id>/<str:action>/', approve_reject_product, name='approve-reject-product')
]

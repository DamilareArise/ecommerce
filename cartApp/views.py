from django.shortcuts import render, get_object_or_404, redirect
from ecommerce.productApp.models import Product
from django.contrib import messages
from django.forms.models import model_to_dict

# Create your views here.

def add_to_cart(request, product_id):
    try:
        
        cart = request.session.get('cart', {})
        # product = get_object_or_404(Product, id = product_id)
        product = Product.objects.get(id = product_id)
        product_id_str = str(product_id)
        
        if product_id_str in cart:
            cart[product_id_str]['quantity'] += 1
        else:
            cart[product_id_str] = {'product': product.product_name, 'price': float(product.price), 'quantity': 1}
            
        request.session['cart'] = cart
        request.session.modified = True  # Ensure session updates
        
        messages.success(request, f'{product.product_name} added to cart successfully')
    except:
        messages.error(request, 'Error adding product to cart')
   
    
    return redirect('home')
    
    

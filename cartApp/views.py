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
   
    
    return redirect('view-cart')


def reduceQuantity(request, product_id):
    
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart and cart[product_id_str]['quantity'] > 1:
        cart[product_id_str]['quantity'] -= 1
        request.session['cart'] = cart
        request.session.modified = True  # Ensure session updates
    else:
        del cart[product_id_str]
        request.session['cart'] = cart
        request.session.modified = True  # Ensure session updates

    return redirect('view-cart')       


def viewCart(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect('home')
    else:
        cart_items = []
        total_price = 0.0
        for product_id, item in cart.items():
            product = get_object_or_404(Product, id = product_id)
            
            subtotal = item['quantity'] * item['price']
            total_price += subtotal

            cart_items.append({
                'product': product,
                'quantity': item["quantity"],
                'price': item["price"],
                'subtotal': subtotal
            })
       
        return render(request, 'cart.html', {'cart_items': cart_items, 'total_price':total_price})

    
    

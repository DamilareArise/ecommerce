from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from ecommerce.userApp.models import Profile
from .decorators import staff_required


# Create your views here.

# def addProduct(request):
    # if request.method == 'POST':
    #     # print(request.POST, "product_details")
    #     # print(request.FILES, "request.FILES")
        
    #     product_name = request.POST.get('product_name')
    #     category = request.POST.get('category')
    #     quantity = request.POST.get('quantity')
    #     price = request.POST.get('price')
    #     image = request.FILES.get('image')

    #     # product = Product(product_name=product_name, category=category, quantity=quantity, price=price, image=image)
    #     # product.save()
        
    #     Product.objects.create(product_name=product_name, category=category, quantity=quantity, price=price, image=image)
        
        
    #     return redirect('home')
    # else:
    #     return render(request, template_name='addProduct.html')
@staff_required
@login_required
def addProduct(request):
    addedby = get_object_or_404(Profile, user_id=request.user.id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            form = product_form.save(commit=False)
            form.addedby = addedby
            form.save()
        else:
            print(product_form.errors)
        return redirect('home')
        
    else:
        product_form = ProductForm()
        return render(request, template_name='addProduct.html', context={'product_form': product_form})
        
        
    
def home(request):
    products = Product.objects.all().filter(approved=True)
    return render(request, template_name='index.html', context={'all_product': products})

def viewProduct(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, template_name='viewProduct.html', context={'product': product})

@staff_required
@login_required
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, id = product_id )
    product.delete()
    
    return redirect('home')

@staff_required
@login_required
def editProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id) # {name: 'ola'}
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        product.product_name = product_name
        product.category = category
        product.quantity = quantity
        product.price = price
        product.image = image
        
        
        product.save()
        return redirect('home')
    else:
        return render(request, template_name='viewProduct.html', context={'product': product})

@staff_required            
@login_required
def viewAllProducts(request):
    products = Product.objects.all()
    return render(request, template_name='viewAllProducts.html', context={'all_product': products})

@staff_required
@login_required
def approve_reject_product(request, product_id, action):
    
    product = get_object_or_404(Product, id=product_id)
    if action == 'approve':
        product.approved = True
    elif action == 'reject':
        product.approved = False
    product.save()
    return redirect('view-all-products')
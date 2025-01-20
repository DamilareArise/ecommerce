from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


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

def addProduct(request):
    
    if request.method == 'POST':
        pass
    else:
        product_form = ProductForm()
        return render(request, template_name='addProduct.html', context={'product_form': product_form})
        
        
    
def home(request):
    products = Product.objects.all()
    return render(request, template_name='index.html', context={'all_product': products})

def viewProduct(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, template_name='viewProduct.html', context={'product': product})

def deleteProduct(request, product_id):
    product = get_object_or_404(Product, id = product_id )
    product.delete()
    
    return redirect('home')


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
              
        
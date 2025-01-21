from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(required=False, widget= forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = [
            'product_name',
            'category',
            'quantity',
            'price',
            'image'
        ]
        
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control mb-2'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder':'Quantity'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mb-2'}),
        }
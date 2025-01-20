from django.db import models

# Create your models here.

class Product(models.Model):
    cat = [
        ('Men', 'Men'),
        ('Women', 'Women')
    ]
    
    product_name = models.CharField(max_length=50, null=True)
    category = models.CharField(choices=cat, max_length=50, null=True)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='productImages/', null=True)
from django.db import models
from ecommerce.userApp.models import Profile

# Create your models here.

class Product(models.Model):
    cat = [
        ('Men', 'Men'),
        ('Women', 'Women')
    ]
    
    addedby = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, null=True)
    category = models.CharField(choices=cat, max_length=50, null=True)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='productImages/', null=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.product_name
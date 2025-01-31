from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

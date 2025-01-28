from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.name
from django.db import models


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

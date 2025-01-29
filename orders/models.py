from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('user.User', related_name='user', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Products', related_name='orders', blank=True)   
     
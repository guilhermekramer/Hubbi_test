from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    orders = models.ManyToManyField('orders.Orders', related_name='orders', blank=True)
    

from django.shortcuts import render
from rest_framework import viewsets
from products.models import Products
from products.serializers import ProductsSerializer

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
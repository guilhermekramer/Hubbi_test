import re
from django.shortcuts import render
from rest_framework import viewsets
from products.models import Products
from products.serializers import ProductsSerializer
from stock.models import Stock

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == 201:
            Stock.objects.create(product_id=response.data['product_id'], quantity=request.data['product_quantity'])
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)

        if response.status_code == 200:
            Stock.objects.filter(product_id=response.data['product_id']).update(quantity=request.data['product_quantity'])
        return response

        
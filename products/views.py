import io
import re
from django.shortcuts import render
from rest_framework import viewsets
from products.models import Products
from products.serializers import ProductsSerializer
from .tasks import processar_csv
from stock.models import Stock
import csv
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == 201:
            Stock.objects.create(product_id=response.data['product_id'])
        return response
    
    # def update(self, request, *args, **kwargs):
    #     response = super().update(request, *args, **kwargs)

    #     if response.status_code == 200:
    #         Stock.objects.filter(product_id=response.data['product_id']).update(quantity=request.data['product_quantity'])
    #     return response

        
    @action(detail=False, methods=['post'],url_path='upload-csv')
    def products_to_csv(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'No file was submitted'})

        try:
            file = file.read().decode('utf-8')
            processar_csv(file)
            return Response({'message': 'CSV file was processed successfully'})
        except Exception as e:
            return Response({'error': str(e)})
            

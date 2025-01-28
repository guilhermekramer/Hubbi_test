from django.shortcuts import render

from stock.models import Stock
from stock.serializers import StockSerializer
from rest_framework import viewsets

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
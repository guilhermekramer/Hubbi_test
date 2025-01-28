from django.shortcuts import render
from rest_framework import viewsets

from orders.models import Orders
from orders.serializers import OrdersSerializer

# Create your views here.
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

from products.models import Products
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

# class CSVSerializer(serializers.Serializer):
#     arquivo = serializers.FileField()
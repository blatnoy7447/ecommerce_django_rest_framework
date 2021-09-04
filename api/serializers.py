from rest_framework import serializers
from mainapp.models import *


class ProductSerializers(serializers.ModelSerializer):
    """Список продуктов"""
    class Meta:
        model = Products
        fields = ("id", "product_name", "subcategories_id")


class ProductDetailSerializers(serializers.ModelSerializer):
    """Полный продукт"""
    class Meta:
        model = Products
        exclude = ("added_by_merchant", )

from rest_framework import serializers
from mainapp.models import *


class ProductSerializers(serializers.ModelSerializer):
    """Список продуктов"""
    class Meta:
        model = Products
        fields = ("id", "product_name", "subcategories_id")


class ProductDetailSerializers(serializers.ModelSerializer):
    """Полный продукт"""
    # foreignkey id sini urniga "title" ni chiqaramiz
    subcategories_id = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Products
        exclude = ("added_by_merchant", )

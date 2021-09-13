from rest_framework import serializers
from mainapp.models import *


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ProductSerializers(serializers.ModelSerializer):
    """Список продуктов"""
    class Meta:
        model = Products
        fields = ("id", "product_name", "subcategories_id")


class ProductReviewsCreateSerializer(serializers.ModelSerializer):
    """Довавление отзыва"""
    class Meta:
        model = ProductReviews
        fields = "__all__"


class ProductReviewsSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = ProductReviews
        fields = ("review", "product_id", "children")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Полный продукт"""
    # foreignkey id sini urniga "title" ni chiqaramiz
    subcategories_id = serializers.SlugRelatedField(slug_field="title", read_only=True)
    reviews = ProductReviewsSerializer(many=True)

    class Meta:
        model = Products
        exclude = ("added_by_merchant", )


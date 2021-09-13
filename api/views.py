from rest_framework import generics

from mainapp.models import Products
from .serializers import (
    ProductSerializers,
    ProductDetailSerializer,
    ProductReviewsCreateSerializer
)


class ProductListView(generics.ListAPIView):
    """Вывод списка продуктов"""
    serializer_class = ProductSerializers

    def get_queryset(self):
        products = Products.objects.all()
        return products


class ProductDetailView(generics.RetrieveAPIView):
    """Вывод продукта"""
    queryset = Products.objects.all()
    serializer_class = ProductDetailSerializer


class ProductReviewsCreateView(generics.CreateAPIView):
    """Добавление отзыва к продукту"""
    serializer_class = ProductReviewsCreateSerializer

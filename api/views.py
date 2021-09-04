from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.models import Products
from .serializers import ProductSerializers, ProductDetailSerializers


class ProductListView(APIView):

    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = Products.objects.get(id=pk)
        serializer = ProductDetailSerializers(product)
        return Response(serializer.data)

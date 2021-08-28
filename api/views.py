from rest_framework import generics
from mainapp import models
from .serializers import CategoriesSerializer


class ListCategory(generics.ListCreateAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = CategoriesSerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = CategoriesSerializer

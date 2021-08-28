from rest_framework import serializers
from mainapp import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Categories

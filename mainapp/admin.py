from django.contrib import admin
from .models import Categories, SubCategories, Products, ProductDetails

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(ProductDetails)

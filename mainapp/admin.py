from django.contrib import admin
from .models import Categories, SubCategories, Products, ProductDetails, ProductReviews

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(ProductDetails)
admin.site.register(ProductReviews)

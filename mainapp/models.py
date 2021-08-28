from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type_choices = ((1, "Admin"), (2, "Staff"), (3, "Merchant"), (4, "Customer"))
    user_type = models.CharField(max_length=255, choices=user_type_choices, default=1)


class AdminUser(models.Model):
    profile_pic = models.FileField()
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class StaffUser(models.Model):
    profile_pic = models.FileField()
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class MerchantUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class CustomerUser(models.Model):
    auth_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class SubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    product_max_price = models.CharField(max_length=255)
    product_discount_price = models.CharField(max_length=255)
    product_description = models.TextField()
    product_long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    added_by_merchant = models.ForeignKey(MerchantUser, on_delete=models.CASCADE)
    in_stock_total = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1)


class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

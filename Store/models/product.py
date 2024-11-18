from django.db import models
from .categories import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to="Upload/Images/")

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    # chaining categories

    @staticmethod
    def get_all_products_by_id(categories_id):
        if categories_id:
            return Product.objects.filter(category=categories_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_cart_products_by_id(ids):
        return Product.objects.filter(id__in = ids)
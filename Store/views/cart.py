from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from Store.models.customer import Customer
from django.views import View
from Store.models.product import Product

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_cart_products_by_id(ids)
        print(products)
        return render(request, "cart.html", {'products':products})


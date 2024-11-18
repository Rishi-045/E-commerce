from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from Store.models.customer import Customer
from django.views import View
from Store.models.product import Product
from Store.models.orders import Order

class Order_c(View):
    def get(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_cart_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()

        request.session['cart'] = {}
        return render(request, 'order-confirmation.html')

class Qr_pg(View):
    def get(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_cart_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()

        request.session['cart'] = {}
        return render(request, 'qr-page.html')
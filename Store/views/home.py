from django.shortcuts import render, redirect
from Store.models.product import Product
from Store.models.categories import Category
from django.views import View



# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')


    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']= {}
        products = None
        categories = Category.get_all_categories()
        categories_id = request.GET.get('categories')  # now we have to do read these categories on server
        if categories_id:
            products = Product.get_all_products_by_id(categories_id)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are: ', request.session.get('email'))
        return render(request, 'index.html', data)



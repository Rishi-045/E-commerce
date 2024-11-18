from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from Store.models.customer import Customer
from django.views import View

# Show alert messages form submit
from django.contrib import messages

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST.get
        first_name = postData('FirstName')
        last_name = postData('LastName')
        email = postData('Email')
        phone = postData('Phone')
        password = postData('Password')

        # validations
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # create customer object
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password,
        )
        error_message = self.validateCustomer(customer)

        # savings

        if not error_message:
            print(first_name, last_name, email, phone, password)
            # password hashing
            customer.password = make_password(customer.password)
            customer.register()

            # submit
            messages.success(request, "Account Created Successfully")

            return redirect('signup')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)


    def validateCustomer(self, customer):
        error_message = None
        c = customer
        if not c.first_name:
            error_message = "First Name Required !!"
        elif not c.last_name:
            error_message = "Last Name Required !!"
        elif not c.phone:
            error_message = "Phone no. Required !!"
        elif len(c.phone) != 10:
            error_message = "Phone no. must be 10 digits only !!"
        elif not c.password:
            error_message = "Password Required !!"
        elif len(c.password) < 8:
            error_message = "Password must be at least 8 characters !!"
        # checking email if it is already exists or not
        elif customer.isExists():
            error_message = 'Email Already Exists !'
        return error_message

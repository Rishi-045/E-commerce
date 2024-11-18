from django.contrib import admin
from django.urls import path
from .views import home, login, signup, cart, checkout, order, order_c
from .middlewares.auth import auth_middleware

urlpatterns = [
    path("", home.Index.as_view(),name="homepage"),
    path("signup", signup.Signup.as_view(), name='signup'),
    path("login", login.Login.as_view(), name='login'),
    path("logout", login.logout, name='logout'),
    path("cart", cart.Cart.as_view(), name='cart'),
    path("checkout", checkout.Checkout.as_view(), name='checkout'),
    path("order", auth_middleware(order.OrderView.as_view()), name='order'),
    path('order-confirmation', order_c.Order_c.as_view(), name='order-confirmation'),
    path('qr-page', order_c.Qr_pg.as_view(), name='qr-page'),
]
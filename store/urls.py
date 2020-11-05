from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

# mapping of page for this first we have to create view in views.py
urlpatterns = [
    path('',Index.as_view(), name='homepage'),
    path('signup',Signup.as_view(), name='signup'),  # for reaching on particular page
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('checkout',CheckOut.as_view(),name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]


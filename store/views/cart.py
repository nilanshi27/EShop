from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import  Product



# this is used to serve page using class,this is class based view
class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_Product_by_id(ids)
        return render(request, 'cart.html',{'products':products})


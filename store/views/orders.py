from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import  Product
from store.models.orders import  Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator



# this is used to serve page using class,this is class based view
class OrderView(View):
    # @method_decorator(auth_middleware) alliter of this is in urls.py
    def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_order_by_cutomer(customer)
        #orders=orders.reverse()
        return render(request,'orders.html',{'orders':orders})

from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import  Product
from store.models.orders import  Order



# this is used to serve page using class,this is class based view
class CheckOut(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_Product_by_id(list(cart.keys()))
        print(address,phone,customer,cart,products)

        for product in products:
            order=Order(customer=Customer(id=customer),
                        product=product,
                        price=product.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart']={}
        return redirect('cart')


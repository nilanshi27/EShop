from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import categorie
from django.views import View

# Create your views for index page here.
class Index(View):
    # for post which is for add to cart
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        #this is to save the object into cart showing how many products are there

        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1

                else:
                    cart[product] = quantity +1

            else:
                cart[product]=1
        else:
            cart={}
            cart[product] = 1
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('homepage')



    #for get
    def get(self,request):
        cart=request.session.get('cart') #for deciding if cart is empty or not
        if not cart:
            request.session['cart']={}
        products = None
        # products = Product.get_all_products()
        # this is used to fetch product
        categories = categorie.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'index.html', data)








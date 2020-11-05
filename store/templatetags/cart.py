# this is for filter

from django import template

register = template.Library()


# this will show  if product is already in cart or not
@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


#to count how many products are there
@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 


#price multiplyby number of product
@register.filter(name='price_total')   
def price_total(product  , cart): 
    return product.price*cart_quantity(product,cart)
    

#totalcart price
@register.filter(name='total_cart_price')   
def total_cart_price(products,cart): 
    sum=0
    for p in products:
        sum=sum+price_total(p,cart)
    return sum
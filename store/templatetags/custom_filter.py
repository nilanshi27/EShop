# this is for filter

from django import template

register = template.Library()


# this will show  if product is already in cart or not
@register.filter(name='currency')
def currency(number):
    return "₹"+str(number)


@register.filter(name='multiply')
def multiply(number,number1):
    return number*number1
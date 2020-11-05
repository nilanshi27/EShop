from django.db import models
from .product import Product
from .customer import Customer
import datetime
#this class is formed to create a model in databse
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=12,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    completed=models.BooleanField(default=False)


    def placeOrder(self):
        self.save()



    #this shows which order is placed by which customer in this \ says that line is not completed yet
    @staticmethod
    def get_order_by_cutomer(customer_id):
        return Order\
            .objects\
            .filter(customer=customer_id)\
            .order_by('-date')
    # this is for showing order acc to date


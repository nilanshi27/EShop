from django.db import models
from .category import categorie
#this forms table in database
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    categorie=models.ForeignKey(categorie, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200 , default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')



#extraction product for show in cart
    @staticmethod
    def get_Product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
#this is used to get filtered data using id
    @staticmethod
    def get_all_products_by_categoryid(categorie_id):
        if categorie_id:
            return Product.objects.filter(categorie= categorie_id)
        else:
            return Product.get_all_products();

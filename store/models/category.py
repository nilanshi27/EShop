from django.db import models
#this class is formed to create a model in databse
class categorie(models.Model):
    name=models.CharField(max_length=20)
#this method will get all the details of categories
    @staticmethod
    def get_all_categories():
        return categorie.objects.all()

    def __str__(self):
        return self.name

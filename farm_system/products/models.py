from django.db import models
from polymorphic.models import PolymorphicModel

from farmer.models import Farmer

# Create your models here.
#to get more info on the polymorphic, use the link https://django-polymorphic.readthedocs.io/en/stable/quickstart.html#using-polymorphic-models
class Product(PolymorphicModel):
    id = models.IntegerField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)


class Food(Product):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class Fertilizer(Product):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Pesticide(Product):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    def __str__(self):
        return self.name

class Machinery(Product):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Tools(Product):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.FloatField()

    def __str__(self):
        return self.name

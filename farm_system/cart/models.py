from django.db import models

# Create your models here.
from consumer.models import Consumer
from products.models import *



class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    is_checked_out = models.BooleanField(default=False)
    amount = models.FloatField()


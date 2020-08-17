from django.db import models
from payment_items.models import Payment_items
# Create your models here.

class Payments(models.Model):
    id = models.IntegerField(primary_key=True)
    payment_items = models.ForeignKey(Payment_items, on_delete=models.CASCADE)
    paid_amount = models.FloatField(null=False)
    
    
    class Meta:
        pass
       





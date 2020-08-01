from django.db import models
from cart.models import Cart


# Create your models here.
class Payment_items(models.Model):
    id = models.IntegerField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    is_paid = models.BinaryField(default=False)

    class Meta:
        pass

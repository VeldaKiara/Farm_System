from django.db import models

# Create your models here.
from datetime import datetime
from django.utils import timezone
from accounts.models import CustomUser
from consumer.models import Consumer

class Farmer(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   
 
    

class Selling(models.Model):
	consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
	farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
	is_approved = models.BooleanField(default=False)
	date = models.DateField(default=timezone.now)
   
    
       
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        pass
    
  
    def __str__(self):
        self.username
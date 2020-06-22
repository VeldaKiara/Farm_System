from django.db import models

# Create your models here.
 from accounts.models import CustomUser
class Consumer(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.id}'
		
		
		
		
from django import forms
from accounts.models import CustomUser
from farmer.models import Farmer

class  FarmerForms(models.Model):
   user_id = forms.ModelChoiceField(CustomUser.objects.all())
    

    class Meta:
    	model = Farmer
    	fields = (user_id)
        pass
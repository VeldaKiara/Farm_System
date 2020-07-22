from django import forms
from accounts.models import CustomUser
from consumer.models import Consumer


class ConsumerForms(forms.ModelForm):
   user_id = forms.ModelChoiceField(CustomUser.objects.all())


    class Meta: 
    	model = Consumer
    	fields = ('user_id')
        pass 
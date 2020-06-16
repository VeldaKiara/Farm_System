from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import CustomUser


USER_TYPES =[
     (0, 'Farmer'),
     (1, 'Consumer'),
]

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username', max_length=45)
    email = forms.EmailField(label = 'Email Address', max_length=250)
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    user_type = forms.IntegerField(widget=forms.Select(choices=USER_TYPES))
        
        
        
        
     
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'user_type') 
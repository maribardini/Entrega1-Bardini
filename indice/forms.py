from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MiCreacionUser(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput())
    password2= forms.CharField(label='Repetir Contraseña',widget= forms.PasswordInput())
    first_name = forms.CharField(label='Nombre', max_length=20, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30)
        
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_text = {k:'' for k in fields}
        
        
        
class MiEdicionUser(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput())
    password2= forms.CharField(label='Repetir Contraseña',widget= forms.PasswordInput())  
    first_name = forms.CharField(label='Nombre', max_length=20, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30)
    


    
    

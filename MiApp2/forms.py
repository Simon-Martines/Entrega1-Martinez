from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class CrearTrabajoForm(forms.Form):

    nombre = forms.CharField(min_length=5,max_length=40)
    sueldo = forms.IntegerField()

class CrearEmpleadoForm(forms.Form):

    nombre= forms.CharField(min_length=2,max_length=40)
    apellido= forms.CharField(min_length=2,max_length=40)
    email= forms.EmailField()
    profesion= forms.CharField(min_length=2,max_length=30)

class CrearClientesForm(forms.Form):
    
    nombre= forms.CharField(min_length=2,max_length=40)
    apellido= forms.CharField(min_length=2,max_length=40)
    email= forms.EmailField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir La Contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']

        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    
    email =forms.EmailField(label="modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir La Contraseña', widget=forms.PasswordInput)
    
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}
        
# class AvatarForm(AvatarForm):
    
    # email =forms.EmailField(label="modificar E-mail")
    # password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repetir La Contraseña', widget=forms.PasswordInput)
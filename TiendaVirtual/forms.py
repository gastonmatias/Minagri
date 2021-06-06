from django import forms

# se importa el form de creacion de usuario que django tiene x defecto
from django.contrib.auth.forms import UserCreationForm 

#se importan los datos de usuario qe existe por defecto en django
from django.contrib.auth.models import User

#se creara un formulario de registro de usuario customizado, django posee uno por defecto
# llamado "userCreationForm", pero tiene opciones limitadas, para customizarlo se creará una clase
# y se pasara x parametro este form ya prediseñado (usando herencia), 
# luego simplemente se agregaran los campos que uno quisiera

class CustomUserCreationForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


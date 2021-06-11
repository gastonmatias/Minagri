from django.forms import fields
from TiendaVirtual.models import Agricultor
from django import forms

#Formulario Registro Agricultor Publicista
class PublicitarioForm(forms.ModelForm):

    class Meta:
        model = Agricultor
        fields = ['nombre','appaterno','apmaterno','rut','nombreComercial','telefono1','telefono2']

#Formulario Registro Agricultor Vendedor
class VendedorForm(forms.ModelForm):

    class Meta:
        model = Agricultor
        fields = ['nombre','appaterno','apmaterno','rut','nombreComercial','telefono1','telefono2','bancoAsociado','nroCuenta']

from django.forms import fields
#se importan los modelos de bd que se usaran como base para crear los forms (desde models.py)
from TiendaVirtual.models import Agricultor, Cliente

#se importa la utilidad de django de formulario x defecto
from django import forms

#a partir de aqui se crearan formularios de registro para cada modelo (agricultorres y clientes)
# heredando las caract de "form" que django contiene x defecto, 
# PERO se adecuará esta plantilla de django segun los campos (atributos) que cada entidad posee
# para ello se crea una subclase ("meta") y en ella se indica que campos tendrá el formulario
# que django creará 

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

# formulario registro Cliente
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre','appaterno','apmaterno','rut','telefono1','telefono2','email']

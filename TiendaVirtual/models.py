from django.db import models

# Create your models here.
class Agricultor(models.Model):
    #requisitos minimos agricultor publicitario-vendedor
    nombre = models.CharField(max_length = 20)
    appaterno = models.CharField(max_length = 20)
    apmaterno = models.CharField(max_length = 20)
    rut = models.CharField(max_length = 12)
    nombreComercial = models.CharField(max_length=25,null='true')
    telefono1 = models.CharField(max_length = 15)
    telefono2 = models.CharField(max_length = 15,null='true')
    
    #requisitos exclusivos agricultor vendedor
    email = models.EmailField(null='true')
    bancoAsociado = models.CharField(max_length = 20,null='true')
    nroCuenta = models.IntegerField(null='true')


class Cliente(models.Model):
    nombre = models.CharField(max_length = 20)
    appaterno = models.CharField(max_length = 20)
    apmaterno = models.CharField(max_length = 20)
    rut = models.CharField(max_length = 12)
    telefono1 = models.CharField(max_length = 15)
    telefono2 = models.CharField(max_length = 15,null='true')
    email = models.EmailField

class Producto(models.Model):
    nombreProducto = models.CharField(max_length = 20)
    precioKilo = models.IntegerField
    precioKiloMayorista = models.IntegerField(null='true')
    descripcion = models.CharField(max_length=100)


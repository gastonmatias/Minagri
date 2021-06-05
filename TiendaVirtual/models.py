from django.db import models

# Create your models here.
class Productor(models.Model):
    
    #requisitos minimos agricultor publicitario-vendedor
    nombre = models.Charfield(max_lenght = 20)
    appaterno = models.Charfield(max_lenght = 20)
    apmaterno = models.Charfield(max_lenght = 20)
    rut = models.charfield(max_lenght = 12)
    nombreComercial = models.charfield(max_lenght=25,null='true')
    telefono1 = models.Charfield(max_lenght = 20)
    telefono2 = models.Charfield(max_lenght = 20,null='true')
    
    #requisitos exclusivos agricultor vendedor
    email = models.EmailField(null='true')
    bancoAsociado = models.Charfield(max_lenght = 20,null='true')
    nroCuenta = models.IntergerField(null='true')


class Cliente(models.Model):
    nombre = models.Charfield(max_lenght = 20)
    appaterno = models.Charfield(max_lenght = 20)
    apmaterno = models.Charfield(max_lenght = 20)
    rut = models.charfield(max_lenght = 12)
    telefono1 = models.Charfield(max_lenght = 20)
    telefono2 = models.Charfield(max_lenght = 20,null='true')
    email = models.EmailField

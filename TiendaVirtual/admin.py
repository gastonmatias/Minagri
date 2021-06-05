from django.contrib import admin
# from django.db.models.base import Model

# Register your models here.
class Productor(models.Model):
    nombre = models.Charfield(max_lenght = 20)
    appaterno = models.Charfield(max_lenght = 20)
    apmaterno = models.Charfield(max_lenght = 20)
    rut = models.charfield(max_lenght = 12)
    nombreComercial = models.charfield(max_lenght=25,null='true')
    telefono1 = models.Charfield(max_lenght = 20)
    telefono2 = models.Charfield(max_lenght = 20,null='true')
    bancoAsociado = models.Charfield(max_lenght = 20,null='true')
    nroCuenta = models.IntergerField(null='true')




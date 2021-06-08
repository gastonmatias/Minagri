from django.db import models

# Create your models here.
class Agricultor(models.Model):
    #requisitos minimos agricultor publicitario-vendedor
    nombre = models.CharField('Primer Nombre',max_length = 20)
    appaterno = models.CharField('Apellido Paterno',max_length = 20)
    apmaterno = models.CharField('Apellido Materno',max_length = 20)
    rut = models.CharField('Rut (sin puntos y con guión)',max_length = 12)
    nombreComercial = models.CharField('Nombre Comercial',max_length=25,null='true',blank=True)
    telefono1 = models.CharField('Telefono 1',max_length = 15)
    telefono2 = models.CharField('Telefono 2',max_length = 15,null='true',blank=True)
    
    #requisitos exclusivos agricultor vendedor
    email = models.EmailField('Correo Electronico',null='true')
    bancoAsociado = models.CharField(max_length = 20,null='true')
    nroCuenta = models.IntegerField(null='true')

    class Meta:
        verbose_name = 'Agricultor'
        verbose_name_plural = 'Agricultores'
    
    def __str__(self):
        return "{0}, {1}".format(self.appaterno,self.nombre)


class Cliente(models.Model):
    nombre = models.CharField(max_length = 20)
    appaterno = models.CharField(max_length = 20)
    apmaterno = models.CharField(max_length = 20)
    rut = models.CharField(max_length = 12)
    telefono1 = models.CharField(max_length = 15)
    telefono2 = models.CharField(max_length = 15,null='true')
    email = models.EmailField

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return "{0}, {1}".format(self.appaterno,self.nombre)

class Producto(models.Model):
    nombreProducto = models.CharField(max_length = 20)
    precioKilo = models.IntegerField
    precioKiloMayorista = models.IntegerField(null='true')
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombreProducto



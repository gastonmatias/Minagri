from django.db import models
from django.conf import settings

# Create your models here.

# modelo de bd para Agricultor (vendedor y publicitario)
class Agricultor(models.Model):
    #requisitos minimos agricultor publicitario-vendedor
    nombre = models.CharField('Primer Nombre',max_length = 20)
    appaterno = models.CharField('Apellido Paterno',max_length = 20)
    apmaterno = models.CharField('Apellido Materno',max_length = 20)
    rut = models.CharField('Rut (sin puntos y con guión)',max_length = 12)
    nombreComercial = models.CharField('Nombre Comercial',max_length=25,null='true',blank=True)
    telefono1 = models.CharField('Telefono 1',max_length = 15)
    telefono2 = models.CharField('Telefono 2',max_length = 15,null='true',blank=True)
    email = models.EmailField('Correo Electronico',null='true')

    #requisitos exclusivos agricultor vendedor
    bancoAsociado = models.CharField('Banco Asociado',max_length = 20,null='true',blank=True)
    nroCuenta = models.IntegerField('Nro Cuenta',null='true',blank=True)

    class Meta:
        verbose_name = 'Agricultor'
        verbose_name_plural = 'Agricultores'
    
    def __str__(self):
        return "{0}, {1}".format(self.appaterno,self.nombre)


# modelo bd para Cliente
class Cliente(models.Model):
    nombre = models.CharField('Nombre',max_length = 20)
    appaterno = models.CharField('Apellido Paterno',max_length = 20)
    apmaterno = models.CharField('Apellido Materno',max_length = 20)
    rut = models.CharField('Rut (sin puntos, con guion)',max_length = 12)
    telefono1 = models.CharField('Telefono 1',max_length = 15)
    telefono2 = models.CharField('Telefono 2',max_length = 15,null='true',blank=True)
    email = models.EmailField('Correo electronico')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return "{0}, {1}".format(self.appaterno,self.nombre)

class Producto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    nombreProducto = models.CharField('Nombre Producto',max_length = 20)
    precioKilo = models.IntegerField('Precio Kg',null=True)
    precioKiloMayorista = models.IntegerField('Precio Kg Mayorista',null='true')
    descripcion = models.CharField('Descripcion',max_length=100)
    imagen = models.ImageField('Fotografia (Opcional)',upload_to='productos',null=True, blank='True')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombreProducto



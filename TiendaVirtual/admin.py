from django.contrib import admin

#import de modelos de bd propios
from TiendaVirtual.models import Cliente, Producto, Agricultor

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Agricultor)


    






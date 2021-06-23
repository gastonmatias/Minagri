"""Minagri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#imports de views.py
from TiendaVirtual.views import agregarProducto, registrarCliente, registrarPublicitario, registrarVendedor, listarProductos

urlpatterns = [
    #url del sitio administrativo de django
    path('admin/', admin.site.urls),

    # url propios de la app Minagri
        # parametros en "()":
        # 1) url tal cual la vera el usuario en la web
        # 2) nombre de la funcion a la cual hace referencia (de views.py)
        # 3) nombre dado a la url (parametro opcional, es util para usarlo en 
        # redireccionamientos, por ejemplo en los "<nav>" de un html ) 
    path('registro-publicitario/', registrarPublicitario, name='registrarPublicitario'),
    path('registro-vendedor/', registrarVendedor, name='registrarVendedor'),
    path('registro-cliente/', registrarCliente, name='registrarCliente'),
    path('agregar-producto/', agregarProducto, name='agregarProducto'),
    path('listar-productos/', listarProductos, name='listarProductos'),

]

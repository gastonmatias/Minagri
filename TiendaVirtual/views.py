#importaciones propias de django, necesarias para poder plasmar paginas html
from TiendaVirtual.models import Producto
from django.shortcuts import redirect, render

#se importan los formularios creados en forms.py
from TiendaVirtual.forms import PublicitarioForm, VendedorForm, ClienteForm, ProductoForm

# Create your views here.
def registrarPublicitario(request):
    
    #se instancia el form creado en forms.py para incrustarlo en registro.html
    data = {
        'form': PublicitarioForm()
    }

    # los inputs del formulario de registro rellenados por algun usuario 
    # llegan devuelta a esta vista "def registrarPublicitario(request)", 
    
    # ahora se busca qe si los datos de estos inputs
    # son validados mediante el metodo post, entonces guardará estos datos
    # en la bd
    if request.method == 'POST':
        #se crea variable formulario con los datos contenidos en POST
        formulario = PublicitarioForm(data=request.POST, files=request.FILES)#este POST = diccionario de datos
        
        #si pasa la prueba de metodo post + SI pasa validaciones de form.. 
        if formulario.is_valid():
            formulario.save() # se guarda el contenido en la bd!
            data["mensaje"] = "Registro Exitoso!"
        # si pasa la prueba de metodo post + NO pasa validaciones de form...
        else:
            data["form"] = formulario #se sobreescribe el form en el html

    
    return render (request,'registro-publicitario.html',data)#'data' se pasa como 3ra parametro para qe se imprima el form en el html

def registrarVendedor(request):
    
    data = {
        'form': VendedorForm()
    }

    if request.method == 'POST':
        formulario = PublicitarioForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Exitoso!"
        else:
            data["form"] = formulario 

    return render (request,'registro-vendedor.html',data)

def registrarCliente(request):
    
    data = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Exitoso!"
        else:
            data["form"] = formulario 

    return render (request,'registro-cliente.html',data)

def agregarProducto(request):

    data = {
        'form': ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)#files es para la imagen

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto guardado correctamente!"
        else:
            data["form"] = formulario 

    return render(request,'producto/agregar.html',data)

def listarProductos(request):

    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }

    return render(request, 'producto/listar.html',data)
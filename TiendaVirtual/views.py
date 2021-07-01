#importaciones propias de django, necesarias para poder plasmar paginas html
from TiendaVirtual.models import Producto
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.views.generic import ListView, FormView, View

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

class ReservaList(ListView):
    model = Producto
    
    def get_queryset(self,*args, **kwargs):
        # usuario admin podra ver TODAS las reservas
        if self.request.user.is_staff:
            producto_list = Producto.objects.all()
            return producto_list

        # usuario normal solo podra ver SUS PROPIAS reservas
        else:
            producto_list = Producto.objects.filter(user=self.request.user)
            return producto_list

def modificarProducto(request, id):
    
    producto = get_object_or_404(Producto, id=id) 

    data = {
        'form' : ProductoForm(instance=producto)#se instancia un formulario rellenado con datos
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)#se pasa la instancia nuevamente para obtener la id del producto a modificar  
        if formulario.is_valid:
            formulario.save()
            return redirect(to='listarProductos')
        data['form'] = formulario
    return render(request,'producto/modificar.html',data)

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id) 
    producto.delete()
    return redirect (to='listarProductos')

def home(request):
    return render(request,'index.html')


#######################################3##################
#########################################################
class AgregarProducto2(View):
    def get(self,request):
        form = ProductoForm

        data = {
            'form': ProductoForm
        }
        return render(request,'producto/agregar.html',data)

    def post(self,request):
        form = ProductoForm(request.POST,request.FILES)
    

        if form.is_valid():
            data = form.cleaned_data
        
        nuevo_producto = Producto.objects.create(
            user = self.request.user,
            nombreProducto = data['nombreProducto'],
            precioKilo = data['precioKilo'],
            precioKiloMayorista = data['precioKiloMayorista'],
            descripcion = data['descripcion'],
            imagen = data['imagen']
            )
        nuevo_producto.save()
        return redirect (to='listarProductos')
        #return render(request, 'producto/listar.html')
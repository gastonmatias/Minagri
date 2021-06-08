from django.shortcuts import redirect, render
from TiendaVirtual.forms import PublicitarioForm

# Create your views here.
def registrarPublicitario(request):
    
    #se instancia el form creado en forms.py para incrustarlo en registro.html
    data = {
        'form': PublicitarioForm()
    }

    #los inputs del formulario de registro rellenados por algun usuario 
    # llegan devuelta a esta vista "def registrarPublicitario(request)", 
    
    # ahora se busca qe si los datos de estos inputs
    # son validados mediante el metodo post, entonces guardará estos datos
    # en la bd
    if request.method == 'POST':
        #se crea variable formulario con los datos contenidos en POST
        formulario = PublicitarioForm(data=request.POST, files=request.FILES)#este POST = diccionario de datos
        
        #si pasa la prueba de metodo post + SI pasa validaciones de form.. 
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Exitoso!"
        # si pasa la prueba de metodo post + NO pasa validaciones de form...
        else:
            data["form"] = formulario #se sobreescribe el form

    
    return render (request,'registro-publicitario.html',data)
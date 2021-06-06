from django.shortcuts import redirect, render

#para utilidad de formulario de registro desde forms.py
from .forms import CustomUserCreationForm

# funciones propias de django qe permiten autenticar un usuario
from django.contrib.auth import authenticate, login

# Create your views here.
def registro(request):
    
    #se instancia el form creado en forms.py para incrustarlo en registro.html
    data = {
        'form': CustomUserCreationForm()
    }

    # ahora se determina qe si los datos de estos inputs
    # son validados mediante el metodo post, entonces guardará estos datos
    # en la bd
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(username=formulario.cleaned_data["username"])

            #luego de crear exitosamente la cuenta, redirecciona a index
            return redirect(to='home')
        data["form"] = formulario

    return render (request,'registro.html',data)
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Usuarios


def Herramienta_Usuario(request):

    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        if form.is_valid():
            nuevo = Usuarios(
                form.cleaned_data['email'],
                form.cleaned_data['nombre'],
                form.cleaned_data['contraseña'],
                form.cleaned_data['legajo']
            )
            return HttpResponseRedirect(reverse('Usuario'))  
    else:
        form = forms.FormularioPersona()
    aux_Usuarios=Usuarios.obtener_Usuario()
    Usuarios=[]
    for _Usuario in aux_Usuarios:
        Usuarios.append(list(_Usuario))

    return render(request, 'my_APP/Usuario.html', {'form': form, 'Usuarios': Usuarios})

def Usuario_delete(request,dni):
    Usuarios.eliminar_Personas(dni)
    return redirect('/Usuario/')

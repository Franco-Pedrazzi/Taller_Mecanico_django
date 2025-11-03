from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import cliente,Persona



def Herramienta_Cliente(request):

    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        if form.is_valid():
            nuevo = cliente(
                form.cleaned_data['dni'],
                form.cleaned_data['nombre'],
                form.cleaned_data['apellido'],
                form.cleaned_data['tel'],
                form.cleaned_data['dir']
            )
            return HttpResponseRedirect(reverse('cliente'))  
    else:
        form = forms.FormularioPersona()
    aux_clientes=cliente.obtener_Cliente()
    clientes=[]
    for _cliente in aux_clientes:
        clientes.append(list(_cliente))
    
    return render(request, 'my_APP/cliente.html', {'form': form, 'clientes': clientes})

def cliente_delete(request,dni,tabla):
    Persona.eliminar_Personas(dni)
    return redirect(f'/{tabla}/')

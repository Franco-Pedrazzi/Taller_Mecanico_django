from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from myapp import forms
from pys.classes import cliente

lista_clientes = []

def Herramienta_Cliente(request):
    global lista_clientes

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
            lista_clientes.append(nuevo)
            return HttpResponseRedirect(reverse('cliente'))  
    else:
        form = forms.FormularioPersona()


    clientes = [
        {
            "id": i+1,
            "dni": c.dni,
            "nombre": c.nombre,
            "apellido": c.apellido,
            "tel": c.tel,
            "dir": c.dir
        }
        for i, c in enumerate(lista_clientes)
    ]

    return render(request, 'my_APP/cliente.html', {'form': form, 'clientes': clientes})

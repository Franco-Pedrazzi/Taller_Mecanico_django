from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Empleado,Persona



def Herramienta_Empleado(request):

    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        if form.is_valid():
            nuevo = Empleado(
                form.cleaned_data['dni'],
                form.cleaned_data['nombre'],
                form.cleaned_data['apellido'],
                form.cleaned_data['tel'],
                form.cleaned_data['dir']
            )
            return HttpResponseRedirect(reverse('Empleado'))  
    else:
        form = forms.FormularioPersona()
    aux_Empleados=Empleado.obtener_Empleado()
    Empleados=[]
    for _Empleado in aux_Empleados:
        Empleados.append(list(_Empleado))

    return render(request, 'my_APP/Empleado.html', {'form': form, 'Empleados': Empleados})

def Empleado_delete(request,dni):
    Persona.eliminar_Personas(dni)
    return redirect('/Empleado/')

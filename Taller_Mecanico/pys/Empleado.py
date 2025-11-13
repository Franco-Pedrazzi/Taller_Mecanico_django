from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Empleados,Persona



def Herramienta_Empleado(request):
    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        modo = request.POST.get("modo")
        if form.is_valid() and modo == "agregar":
            nuevo = Empleados(
                form.cleaned_data['dni'],
                form.cleaned_data['nombre'],
                form.cleaned_data['apellido'],
                form.cleaned_data['tel'],
                form.cleaned_data['dir']
            )
            
        if modo == "editar" and form.is_valid():
        
            Persona.actualizar_Personas(
                form.cleaned_data['dni'],
                form.cleaned_data['nombre'],
                form.cleaned_data['apellido'],
                form.cleaned_data['tel'],
                form.cleaned_data['dir']
            )
        return HttpResponseRedirect(reverse('Empleado'))  
    else:
        form = forms.FormularioPersona()

    aux_Empleados=Empleados.obtener_Empleado()
    Empleado=[]
    for _Empleado in aux_Empleados:
        Empleado.append(list(_Empleado))

    return render(request, 'my_APP/Empleado.html', {'form': form, 'Empleados': Empleado})

def Empleado_delete(request,dni):
    Persona.eliminar_Personas(dni)
    return redirect('/Empleado/')

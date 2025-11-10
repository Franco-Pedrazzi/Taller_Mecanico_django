from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Repuestos,Persona



def Herramienta_Repuesto(request):
    if request.method == "POST":
        form = forms.FormularioRepuesto(request.POST)
        modo = request.POST.get("modo")
        if form.is_valid() and modo == "agregar":
            Repuestos.insertar_repuesto(
                form.cleaned_data['nombre'],
                form.cleaned_data['precio_x_unidad'],
                form.cleaned_data['cantidad']
            )
             
        if modo == "editar" and form.is_valid():
        
            Repuestos.actualizar_repuesto(
                form.cleaned_data['nombre'],
                form.cleaned_data['precio_x_unidad'],
                form.cleaned_data['cantidad']
            )
        return HttpResponseRedirect(reverse('Repuesto')) 
    else:
        form = forms.FormularioRepuesto()
    aux_Repuestos=Repuestos.obtener_Repuesto()
    _Repuestos=[]
    for _Repuesto in aux_Repuestos:
        _Repuestos.append(list(_Repuesto))

    return render(request, 'my_APP/Repuesto.html', {'form': form, 'Repuestos': _Repuestos})

def Repuesto_delete(request,dni):
    Persona.eliminar_Personas(dni)
    return redirect('/Repuesto/')

from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Repuestos,Persona



def Herramienta_Repuesto(request):

    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        if form.is_valid():
            nuevo = Repuestos(
                form.cleaned_data['nombre'],
                form.cleaned_data['precio_x_unidad'],
                form.cleaned_data['cantidad']
            )
            return HttpResponseRedirect(reverse('Repuesto'))  
    else:
        form = forms.FormularioPersona()
    aux_Repuestos=Repuestos.obtener_Repuesto()
    Repuestos=[]
    for _Repuesto in aux_Repuestos:
        Repuestos.append(list(_Repuesto))

    return render(request, 'my_APP/Repuesto.html', {'form': form, 'Repuestos': Repuestos})

def Repuesto_delete(request,dni):
    Persona.eliminar_Personas(dni)
    return redirect('/Repuesto/')

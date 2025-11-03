from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Presupuestos



def Herramienta_Presupuesto(request):

    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        if form.is_valid():
            nuevo = Presupuestos(
                form.cleaned_data['matricula'],
                form.cleaned_data['repuesto'],
                form.cleaned_data['cantidad'],
                form.cleaned_data['legajo'],
                form.cleaned_data['precio'],
                form.cleaned_data['id']
            )
            return HttpResponseRedirect(reverse('Presupuesto'))  
    else:
        form = forms.FormularioPersona()
    aux_Presupuestos=Presupuestos.obtener_Presupuesto()
    Presupuestos=[]
    for _Presupuesto in aux_Presupuestos:
        Presupuestos.append(list(_Presupuesto))

    return render(request, 'my_APP/Presupuesto.html', {'form': form, 'Presupuestos': Presupuestos})

def Presupuesto_delete(request,dni):
    Presupuestos.eliminar_Personas(dni)
    return redirect('/Presupuesto/')

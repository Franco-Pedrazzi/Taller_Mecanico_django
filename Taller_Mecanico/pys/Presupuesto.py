from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Presupuestos, FichaTecnica,Vehiculos


def Herramienta_Presupuesto(request,matricula):
    form = forms.FormularioReparacion(request.POST)

    if request.method == "POST":
        if form.is_valid():

            Presupuestos.insertar_Presupuestos(
                matricula,
                form.cleaned_data['repuesto'],
                float(form.cleaned_data['cantidad']),
                form.cleaned_data['legajo'],
                float(form.cleaned_data['precio']),
                
            )

            return HttpResponseRedirect(reverse('Presupuesto', kwargs={'matricula': matricula}))


    aux_Presupuestos = Presupuestos.obtener_Presupuesto(matricula)

    _Presupuestos = [list(p) for p in aux_Presupuestos if p]
    print(_Presupuestos)
    return render(request, 'my_APP/Presupuesto.html', {
        'form': form,
        'Presupuestos': _Presupuestos,
        'id':matricula

    })


def Herramienta_Ficha_Tecnica(request):

    aux_Ficha_Tecnicas=FichaTecnica.obtener_FichaTecnica()
    Ficha_Tecnicas=[]
    for _Ficha_Tecnica in aux_Ficha_Tecnicas:
        Ficha_Tecnicas.append(list(_Ficha_Tecnica))

    return render(request, 'my_APP/Ficha_Tecnica.html', {'Ficha_Tecnicas': Ficha_Tecnicas})


def Presupuesto_delete(request, matricula,reparacion):
    Presupuestos.eliminar_Presupuesto(reparacion)
    return redirect(f'/Presupuesto/{matricula}')


def Presupuesto_TotalDelete(request, matricula):
    Presupuestos.eliminar_Todo_Presupuesto(matricula)
    return redirect(f'/Presupuesto/{matricula}')

def insertar_FT(request,matricula):
    FichaTecnica.insertar_FichaTecnica(matricula)
    return redirect(f'/Ficha_Tecnica')
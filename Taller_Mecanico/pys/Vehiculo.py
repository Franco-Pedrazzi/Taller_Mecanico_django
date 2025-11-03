from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import cliente,Vehiculos


def Herramienta_Vehiculos(request,cliente_id):

    if request.method == "POST":
        form = forms.FormularioVehiculo(request.POST)
        if form.is_valid():
            Vehiculos.insertar_Vehiculo(
                form.cleaned_data['matricula'],
                form.cleaned_data['color'],
                form.cleaned_data['modelo'],
                cliente_id
            )
            return redirect(f'/vehicle/{cliente_id}') 
    else:
        form = forms.FormularioVehiculo()
    aux_Vehiculos=Vehiculos.obtener_Vehiculo(cliente_id)
    Vehiculo=[]
    for _Vehiculos in aux_Vehiculos:
        Vehiculo.append(list(_Vehiculos))
    dueño= cliente.obtener_Cliente_filtrada(cliente_id)
    dueño=dueño[0]
    print(dueño)
    return render(request ,'my_APP/Vehiculo.html', {'form': form, 'Vehiculos': Vehiculo ,'dueño':f"{dueño[2]} {dueño[3]}"})

def cliente_delete(request,matricula,cliente_id):
    Vehiculos.eliminar_Vehiculo(matricula)
    return redirect(f'/vehicle/{cliente_id}') 

from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import cliente,Persona,Vehiculos



def Herramienta_Cliente(request):

    if request.method == "POST":
        
        form = forms.FormularioPersona(request.POST)
        modo = request.POST.get("modo")
        if form.is_valid() and modo == "agregar":
            nuevo = cliente(
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
        return HttpResponseRedirect(reverse('cliente'))  
    else:
        form = forms.FormularioPersona()
    aux_clientes=cliente.obtener_Cliente()
    clientes=[]
    for _cliente in aux_clientes:
        clientes.append(list(_cliente))
    
    return render(request, 'my_APP/cliente.html', {'form': form, 'clientes': clientes})


def Herramienta_Vehiculos(request,cliente_id):

    if request.method == "POST":
        form = forms.FormularioVehiculo(request.POST)
        modo = request.POST.get("modo")
        if form.is_valid() and modo == "agregar":
            Vehiculos.insertar_Vehiculo(
                form.cleaned_data['matricula'],
                form.cleaned_data['color'],
                form.cleaned_data['modelo'],
                cliente_id
            )
             
        if modo == "editar" and form.is_valid():
        
            Vehiculos.actualizar_Vehiculo(
                form.cleaned_data['matricula'],
                form.cleaned_data['color'],
                form.cleaned_data['modelo']
            )
        return HttpResponseRedirect(reverse('Vehiculo')) 
    else:
        form = forms.FormularioVehiculo()
    
    aux_Vehiculos=Vehiculos.obtener_Vehiculo(cliente_id)
    Vehiculo=[]
    for _Vehiculos in aux_Vehiculos:
        Vehiculo.append(list(_Vehiculos))
    dueño= cliente.obtener_Cliente_filtrada(cliente_id)
    dueño=dueño[0]
    return render(request ,'my_APP/Vehiculo.html', {'form': form, 'Vehiculos': Vehiculo ,'dueño':f"{dueño[2]} {dueño[3]}",'cliente_id':cliente_id})

def vehiculo_delete(request,matricula,cliente_id):
    Vehiculos.eliminar_Vehiculo(matricula)
    return redirect(f'/vehicle/{cliente_id}') 


def cliente_delete(request,dni,tabla):
    Persona.eliminar_Personas(dni)
    return redirect(f'/{tabla}/')

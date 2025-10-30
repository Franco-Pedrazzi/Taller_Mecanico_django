from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import Provedor,Persona



def Herramienta_Provedor(request):

    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        if form.is_valid():
            nuevo = Provedor(
                form.cleaned_data['dni'],
                form.cleaned_data['nombre'],
                form.cleaned_data['apellido'],
                form.cleaned_data['tel'],
                form.cleaned_data['dir']
            )
            return HttpResponseRedirect(reverse('Provedor'))  
    else:
        form = forms.FormularioPersona()
    aux_Provedors=Provedor.obtener_Provedor()
    Provedors=[]
    for _Provedor in aux_Provedors:
        Provedors.append(list(_Provedor))

    return render(request, 'my_APP/Provedor.html', {'form': form, 'Provedors': Provedors})

def Provedor_delete(request,dni):
    Persona.eliminar_Personas(dni)
    return redirect('/Provedor/')

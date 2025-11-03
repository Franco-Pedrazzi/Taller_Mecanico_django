from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from myapp import forms
from pys.classes import FichaTecnica



def Herramienta_Ficha_Tecnica(request):

    if request.method == "POST":
        form = forms.FormularioPersona(request.POST)
        if form.is_valid():
            nuevo = FichaTecnica(
                form.cleaned_data['dni'],
                form.cleaned_data['nombre'],
                form.cleaned_data['apellido'],
                form.cleaned_data['tel'],
                form.cleaned_data['dir']
            )
            return HttpResponseRedirect(reverse('Ficha_Tecnica'))  
    else:
        form = forms.FormularioPersona()
    aux_Ficha_Tecnicas=FichaTecnica.obtener_Ficha_Tecnica()
    Ficha_Tecnicas=[]
    for _Ficha_Tecnica in aux_Ficha_Tecnicas:
        Ficha_Tecnicas.append(list(_Ficha_Tecnica))

    return render(request, 'my_APP/Ficha_Tecnica.html', {'form': form, 'Ficha_Tecnicas': Ficha_Tecnicas})


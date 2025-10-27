from django.http import HttpResponse 
from django.shortcuts import render
def Herramienta_Ficha_Tecnica(request):

    return render(request, 'my_APP/Ficha_Tecnica.html')


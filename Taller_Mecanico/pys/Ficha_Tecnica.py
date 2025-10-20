from django.http import HttpResponse 

def Herramienta_Ficha_Tecnica(request):

    f = open("templates/Ficha_Tecnica.html", encoding="utf-8") 

    response=HttpResponse (f.read()) 
    f.close() 
    return response 


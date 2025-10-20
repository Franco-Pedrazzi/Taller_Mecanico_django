from django.http import HttpResponse 

def Herramienta_Presupuesto(request):

    f = open("templates/Presupuesto.html", encoding="utf-8") 

    response=HttpResponse (f.read()) 
    f.close() 
    return response 


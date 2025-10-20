from django.http import HttpResponse 

def Herramienta_Repuesto(request):

    f = open("templates/Repuesto.html", encoding="utf-8") 

    response=HttpResponse (f.read()) 
    f.close() 
    return response 


from django.http import HttpResponse 

def Herramienta_Repuesto(request):

    f = open("my_APP/Repuesto.html", encoding="utf-8") 

    response=HttpResponse (f.read()) 
    f.close() 
    return response 


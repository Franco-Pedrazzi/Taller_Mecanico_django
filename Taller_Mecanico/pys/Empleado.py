from django.http import HttpResponse 

def Herramienta_Empleado(request):

    f = open("my_APP/Empleado.html", encoding="utf-8") 

    response=HttpResponse (f.read()) 
    f.close() 
    return response 


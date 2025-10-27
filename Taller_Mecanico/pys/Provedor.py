from django.http import HttpResponse 

def Herramienta_Provedor(request):

    f = open("temmy_APPplates/Provedor.html", encoding="utf-8") 

    response=HttpResponse (f.read()) 
    f.close() 
    return response 


from django.http import HttpResponse 

def index (request): 
 
    f = open("templates/index.html", encoding="utf-8") 
 
    response=HttpResponse (f.read()) 
    f.close() 
    return response 


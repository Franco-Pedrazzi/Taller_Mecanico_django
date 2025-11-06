from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.views import View

def index (request): 
    return render(request, 'my_APP/index.html')

def Logout(request):
    logout(request)
    return redirect('login')

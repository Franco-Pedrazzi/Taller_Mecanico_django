from django.urls import path 
from django.contrib import admin
import Taller_Mecanico.py.views as views
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path("", views.index, name="index") ,
] 

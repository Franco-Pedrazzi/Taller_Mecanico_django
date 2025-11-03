from django.urls import path 
from django.contrib import admin
import pys.views as views
import pys.cliente as cliente
import pys.Empleado as Empleado
import pys.Ficha_Tecnica as Ficha_Tecnica
import pys.Presupuesto as Presupuesto
import pys.Provedor as Provedor
import pys.Repuesto as Repuesto
import pys.Vehiculo as Vehiculo
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path("", views.index, name="index") ,
    path("cliente/", cliente.Herramienta_Cliente, name="cliente") ,
    path('persona/eliminar/<str:dni>/<str:tabla>', cliente.cliente_delete, name='cliente_delete'),
    path("Empleado/", Empleado.Herramienta_Empleado, name="Empleado") ,
    path("Ficha_Tecnica/", Ficha_Tecnica.Herramienta_Ficha_Tecnica, name="Ficha_Tecnica") ,
    path("Ficha_Tecnica/", Presupuesto.Herramienta_Presupuesto, name="Presupuesto") ,
    path("Provedor/", Provedor.Herramienta_Provedor, name="Provedor") ,
    path("Repuesto/", Repuesto.Herramienta_Repuesto, name="Repuesto"), 
    path('vehicle/<int:cliente_id>/', Vehiculo.Herramienta_Vehiculos, name='Vehiculo')
] 

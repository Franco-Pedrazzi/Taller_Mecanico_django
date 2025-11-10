from django.urls import path 
from django.contrib import admin
import pys.views as views
import pys.cliente as cliente
import pys.Empleado as Empleado
import pys.Presupuesto as Presupuesto
import pys.Provedor as Provedor
import pys.Repuesto as Repuesto
import pys.SyL as Syl
from django.contrib.auth import views as auth_views
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path("", views.index, name="index") ,
    path("cliente/", cliente.Herramienta_Cliente, name="cliente") ,
    path('persona/eliminar/<str:dni>/<str:tabla>', cliente.cliente_delete, name='cliente_delete'),
    path("Empleado/", Empleado.Herramienta_Empleado, name="Empleado") ,
    path("Ficha_Tecnica/", Presupuesto.Herramienta_Ficha_Tecnica, name="Ficha_Tecnica") ,
    path("Ficha_Tecnica/<str:matricula>", Presupuesto.insertar_FT, name="insertar_FT") ,
    path("Presupuesto/<str:matricula>", Presupuesto.Herramienta_Presupuesto, name="Presupuesto") ,
    path("Presupuesto/<str:matricula>/delete/<int:reparacion>", Presupuesto.Presupuesto_delete, name="Presupuesto_delete") ,
    path("Presupuesto/<str:matricula>/delete", Presupuesto.Presupuesto_TotalDelete, name="Presupuesto_TotalDelete") ,
    path("Provedor/", Provedor.Herramienta_Provedor, name="Provedor") ,
    path("Repuesto/", Repuesto.Herramienta_Repuesto, name="Repuesto"), 
    path('vehicle/<int:cliente_id>/', cliente.Herramienta_Vehiculos, name='Vehiculo'),
    path('vehicle/<int:cliente_id>/delete/<str:matricula>/', cliente.vehiculo_delete, name='vehiculo_delete'),
    path('logout/', views.Logout, name='logout'),
    path('login/', Syl.login_view, name ='login'),
] 

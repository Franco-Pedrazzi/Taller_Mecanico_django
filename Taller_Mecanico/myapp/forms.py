from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pys.classes import Repuestos,Provedores, Empleados
class FormularioPersona(forms.Form):
  dni=forms.IntegerField(required=True)
  nombre=forms.CharField(required=True)
  apellido=forms.CharField(required=True)
  tel=forms.IntegerField(required=True)
  dir=forms.CharField(required=True)

class FormularioVehiculo(forms.Form):
  matricula=forms.CharField(required=True)
  color=forms.CharField(required=True)
  modelo=forms.CharField(required=True)

class FormularioRepuesto(forms.Form):
  Provedor = forms.ChoiceField(required=True)
  nombre=forms.CharField(required=True)
  precio_x_unidad=forms.IntegerField(required=True)
  cantidad=forms.IntegerField(required=True)
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        provedores = Provedores.obtener_Provedor()
        self.fields['Provedor'].choices = [
            (provedor[0], f"{provedor[2]} ({provedor[0]})") for provedor in provedores
        ]

class FormularioReparacion(forms.Form):
    repuesto = forms.ChoiceField(required=True)
    cantidad = forms.IntegerField(required=True)
    legajo = forms.ChoiceField(required=True)
    precio = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        repuestos = Repuestos.obtener_Repuesto()
        self.fields['repuesto'].choices = [
            (repuesto[0], repuesto[0]) for repuesto in repuestos
        ]
        empleados = Empleados.obtener_Empleado()
        self.fields['legajo'].choices = [
            (empledo[0], f"{empledo[2]} {empledo[3]} ({empledo[0]})") for empledo in empleados
        ]

class FormularioUsuarios(forms.Form):
  email=forms.CharField(required=True)
  nombre=forms.CharField(required=True)
  contraseña=forms.CharField(required=True)
  legajo=forms.IntegerField(required=True)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
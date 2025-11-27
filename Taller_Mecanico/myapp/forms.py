from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pys.classes import Repuestos,Provedores
class FormularioPersona(forms.Form):
  dni=forms.CharField(required=True)
  nombre=forms.CharField(required=True)
  apellido=forms.CharField(required=True)
  tel=forms.CharField(required=True)
  dir=forms.CharField(required=True)

class FormularioVehiculo(forms.Form):
  matricula=forms.CharField(required=True)
  color=forms.CharField(required=True)
  modelo=forms.CharField(required=True)

class FormularioRepuesto(forms.Form):
  print(Provedores.obtener_Provedor())
  Provedor=forms.ChoiceField(choices= [(provedor[0],f"{provedor[2]} ({provedor[0]})") for provedor in Provedores.obtener_Provedor()], required=True)
  nombre=forms.CharField(required=True)
  precio_x_unidad=forms.IntegerField(required=True)
  cantidad=forms.IntegerField(required=True)

class FormularioReparacion(forms.Form):
  repuesto=forms.ChoiceField(choices= [(repuesto[0],repuesto[0]) for repuesto in Repuestos.obtener_Repuesto()], required=True)
  cantidad=forms.IntegerField(required=True)
  legajo=forms.CharField(required=True)
  precio=forms.IntegerField(required=True)


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
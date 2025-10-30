from django import forms

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
  dni_cliente= forms.CharField(required=True)

class FormularioRepuesto(forms.Form):
  nombre=forms.CharField(required=True)
  precio_x_unidad=forms.IntegerField(required=True)
  cantidad=forms.IntegerField(required=True)

class FormularioReparacion(forms.Form):
  matricula=forms.CharField(required=True)
  repuesto=forms.CharField(required=True)
  cantidad=forms.IntegerField(required=True)
  legajo=forms.CharField(required=True)
  precio=forms.IntegerField(required=True)
  id=forms.IntegerField(required=True)

class FormularioUsuarios(forms.Form):
  email=forms.CharField(required=True)
  nombre=forms.CharField(required=True)
  contraseña=forms.CharField(required=True)
  legajo=forms.IntegerField(required=True)

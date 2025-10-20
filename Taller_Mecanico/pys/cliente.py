from django.shortcuts import render
from wtforms import Form, StringField, PasswordField, validators

from pys.classes import cliente
class MyForm(Form):
    dni = StringField('DNI', [validators.Length(min=1, max=10), validators.DataRequired()])
    nombre = StringField('Nombre', [validators.Length(min=1, max=10), validators.DataRequired()])
    apellido = StringField('Apellido', [validators.Length(min=1, max=10), validators.DataRequired()])
    tel = StringField('Teléfono', [validators.Length(max=10)])
    dir = StringField('Dirección', [validators.Length(max=25)])
    

def Herramienta_Cliente(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cliente(dni, nombre, apellido, tel, dir)
            dni = form.cleaned_data['dni']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            tel = form.cleaned_data['tel']
            dir = form.cleaned_data['dir']
            return render(request, 'cliente.html', {'nombre': nombre})
    else:
        form = MyForm()

    return render(request, 'cliente.html', {'form': form})

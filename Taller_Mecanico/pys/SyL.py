from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
def login_view(request):

    if request.method == 'POST':
        # Formulario con los datos del POST
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('/')

        # si el form no es valido => mostrar errores
        messages.error(request, 'Invalid username or password.')
        return render(request, 'my_APP/login.html', {
            'form': form,
            'title': 'Log in'
        })

    else:
        form = AuthenticationForm()
        return render(request, 'my_APP/login.html', {
            'form': form,
            'title': 'Log in'
        })

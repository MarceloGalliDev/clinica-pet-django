# flake8: noqa
# pylint: disable=all
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def login_usuario(request):
    if request.method == 'POST':
        # aqui passamos os dados da requisição
        form_login = AuthenticationForm(data=request.POST)
        # se for validado os dados vamos capturar o username e o password
        if form_login.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # apos isso vamos autenticar o usuario
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('listar_clientes')
            else:
                messages.error(request, "As credenciais estão incorretas!")
                return redirect('login')
    else:
        form_login = AuthenticationForm()
    return render(request, 'autenticacao/login.html', {'form_login': form_login})
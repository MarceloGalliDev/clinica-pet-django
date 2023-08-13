# flake8: noqa
# pylint: disable=all

from django.shortcuts import render
from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoClienteForm
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service


def cadastrar_cliente(request):
    if request.method == "POST":
        # aqui recebemos os dados la do formulario
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            email = form_cliente.cleaned_data["email"]
            cpf = form_cliente.cleaned_data["cpf"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            profissao = form_cliente.cleaned_data["profissao"]
            # aqui vamos validar os dados recebidos de endereco
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                # precisamos criar um endereco primeiro pois para cadastrar um cliente é obrigatório ter um endereço atrelado
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                # aqui persistimos os dados para inserir os dados no banco
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                # criamos um novo objeto cliente com os dados capturados acima
                cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, cpf=cpf, endereco=endereco_bd)
                # aqui persistimos os dados para inserir os dados no banco
                cliente_service.cadastrar_cliente(cliente_novo)
                return redirect('listar_clientes')
    else:
        # aqui significa que ele abriu o formulário para poder digitar
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})
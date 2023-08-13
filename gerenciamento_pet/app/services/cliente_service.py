# flake8: noqa
# pylint: disable=all
from ..models import Cliente


# aqui vamos criar um objeto do tipo cliente e armazenar os campos em sua estrutura
def cadastrar_cliente(cliente):
    Cliente.objects.create(
        nome=cliente.nome,
        email=cliente.email,
        endereco=cliente.endereco,
        cpf=cliente.cpf,
        data_nascimento=cliente.data_nascimento,
        profissao=cliente.profissao
    )
    
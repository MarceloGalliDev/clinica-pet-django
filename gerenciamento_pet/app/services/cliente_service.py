# flake8: noqa
# pylint: disable=all
from ..models import Cliente


# aqui vamos criar um objeto do tipo cliente e armazenar os campos em sua estrutura
def cadastrar_cliente(cliente):
    return Cliente.objects.create(
        nome=cliente.nome,
        email=cliente.email,
        endereco=cliente.endereco,
        cpf=cliente.cpf,
        data_nascimento=cliente.data_nascimento,
        profissao=cliente.profissao
    )


def listar_clientes():
    return Cliente.objects.all()


def listar_cliente_id(id):
    return Cliente.objects.get(id=id)
# pylint: skip-file
# flake8: noqa
from django import forms
from ..models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        #vamos criar o formulario baseado no models Cliente
        model = Cliente
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']
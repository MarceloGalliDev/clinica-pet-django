# pylint: skip-file
# flake8: noqa
from django import forms
from django.forms import TextInput, DateInput
from ..models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']
        # adicionando atributos
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type':'date'}
                )
        }
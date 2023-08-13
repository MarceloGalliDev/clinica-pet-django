# pylint: skip-file
# flake8: noqa
from django import forms
from ..models import EnderecoCliente


class EnderecoClienteForm(forms.ModelForm):
    class Meta:
        #vamos criar o formulario baseado no models Cliente
        model = EnderecoCliente
        fields = ['rua', 'cidade', 'estado']
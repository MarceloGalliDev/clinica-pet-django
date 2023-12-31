# pylint: skip-file
# flake8: noqa
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput
from ..models import Funcionario


# esse UserCreationForm ele ja faz a validação dos campos
class FuncionarioForm(UserCreationForm):
    class Meta:
        model = Funcionario
        fields = UserCreationForm.Meta.fields + ('nome', 'nascimento', 'cargo')
        widgets = {
            'nascimento': DateInput(
                attrs={'type': "date"}
            )
        }

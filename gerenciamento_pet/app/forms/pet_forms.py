# pylint: skip-file
# flake8: noqa
from django import forms
from ..models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'nascimento', 'categoria', 'cor']
        exclude = ['dono', ]

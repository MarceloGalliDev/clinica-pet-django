# flake8: noqa
"""urls directory"""
from django.urls import path
from .views import cliente_views


urlpatterns = [
    path('cadastrar_cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_clientes', cliente_views.listar_clientes, name='listar_clientes'),
]

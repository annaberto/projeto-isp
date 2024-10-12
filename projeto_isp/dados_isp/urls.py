# /Users/raphaelaberto/Documents/TI/ISP/projeto-isp/projeto_isp/dados_isp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registros/', views.listar_registros, name='registros'),

    path('registros/criar/', views.criar_registro, name='criar_registro'),

    path('registros/<int:id>/editar/', views.editar_registro, name='editar_registro'),

    path('registros/deletar/<int:id>/', views.deletar_registro, name='deletar_registro'),
]

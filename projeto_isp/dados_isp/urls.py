from django.urls import path
from . import views

urlpatterns = [
    path('registros/', views.listar_registros, name='listar_registros'),
    path('registros/criar/', views.criar_registro, name='criar_registro'),
    path('registros/editar/<int:id>/', views.editar_registro, name='editar_registro'),
    path('registros/deletar/<int:id>/', views.deletar_registro, name='deletar_registro'),
]

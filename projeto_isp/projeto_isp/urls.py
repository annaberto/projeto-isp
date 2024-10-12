from django.contrib import admin
from django.urls import path
from dados_isp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', views.registros, name='registros'),

    path('registros/criar/', views.criar_registro, name='criar_registro'),

    path('registros/<int:id>/editar/', views.editar_registro, name='editar_registro'),

    path('registros/deletar/<int:id>/', views.deletar_registro, name='deletar_registro'),
]


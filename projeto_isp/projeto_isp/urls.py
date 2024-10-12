from django.contrib import admin
from django.urls import path
from dados_isp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', views.listar_injurias, name='listar_injurias'),
    path('registros/criar/', views.criar_registro, name='criar_registro'),

]

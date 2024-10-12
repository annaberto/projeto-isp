from django.urls import path
from . import views

urlpatterns = [
    path('', views.injurias, name='dados_isp'),
]

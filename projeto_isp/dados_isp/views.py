from django.shortcuts import render
from .models import RegistroIncidente

def listar_injurias(request):
    injurias = RegistroIncidente.objects.all()
    return render(request, 'dados_isp/listar_injurias.html', {'injurias': injurias})


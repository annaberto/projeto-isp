from django.shortcuts import render, redirect
from .models import RegistroIncidente
from .forms import RegistroIncidenteForm

def listar_injurias(request):
    injurias = RegistroIncidente.objects.all()
    return render(request, 'dados_isp/listar_injurias.html', {'injurias': injurias})


def criar_registro(request):
    if request.method == 'POST':
        form = RegistroIncidenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_injurias') 
    else:
        form = RegistroIncidenteForm()
    return render(request, 'dados_isp/criar_registro.html', {'form': form})


def editar_registro(request, id):
    registro = RegistroIncidente.objects.get(id=id)
    if request.method == 'POST':
        form = RegistroIncidenteForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listar_registros')
    else:
        form = RegistroIncidenteForm(instance=registro)
    return render(request, 'editar_registro.html', {'form': form})


def deletar_registro(request, id):
    registro = RegistroIncidente.objects.get(id=id)
    if request.method == 'POST':
        registro.delete()
        return redirect('listar_registros')
    return render(request, 'deletar_registro.html', {'registro': registro})

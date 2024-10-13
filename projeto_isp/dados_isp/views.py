from django.shortcuts import render, redirect, get_object_or_404
from .models import RegistroIncidente
from .forms import RegistroIncidenteForm

def registros(request):
    injurias = RegistroIncidente.objects.all()
    return render(request, 'dados_isp/listar_registros.html', {'injurias': injurias})


def criar_registro(request):
    if request.method == 'POST':
        form = RegistroIncidenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registros') 
    else:
        form = RegistroIncidenteForm()
    return render(request, 'dados_isp/criar_registro.html', {'form': form})


def editar_registro(request, id):
    registro = RegistroIncidente.objects.get(id=id)
    if request.method == 'POST':
        form = RegistroIncidenteForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('registros')
    else:
        form = RegistroIncidenteForm(instance=registro)
    return render(request, 'dados_isp/editar_registro.html', {'form': form})



def deletar_registro(request, id):
    registro = get_object_or_404(RegistroIncidente, id=id)

    if request.method == 'POST':
        registro.delete()
        return redirect('registros') 

    return render(request, 'dados_isp/deletar_registro.html', {'registro': registro})
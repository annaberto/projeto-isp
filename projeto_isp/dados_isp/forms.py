from django import forms
from .models import RegistroIncidente

class RegistroIncidenteForm(forms.ModelForm):
    class Meta:
        model = RegistroIncidente
        fields = ['cisp', 'ano', 'mes', 'titulo', 'sexo', 'cor', 'idade', 'vitimas'] 
        widgets = {
            'ano': forms.NumberInput(attrs={'min': '1900', 'max': '2100'}),
            'mes': forms.NumberInput(attrs={'min': '1', 'max': '12'}),
            'titulo': forms.Select(choices=RegistroIncidente.titulo_choices),
            'sexo': forms.Select(choices=RegistroIncidente.sexo_choices),
            'cor': forms.Select(choices=RegistroIncidente.cor_choices),
            'idade': forms.Select(choices=RegistroIncidente.idade_choices),
        }

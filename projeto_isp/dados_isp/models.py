from django.db import models

import pandas as pd

class RegistroIncidente(models.Model):
    cisp = models.IntegerField()

    ano = models.IntegerField()

    mes = models.IntegerField()

    titulo_choices = [
      ("Preconceito de Raça ou de Cor", "Preconceito de Raça ou de Cor"),
      ("Injúria por preconceito", "Injúria por preconceito")
    ]
    titulo = models.CharField(max_length=255, choices=titulo_choices)

    sexo_choices = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Não informado', 'Não informado')
    ]
    sexo = models.CharField(max_length=50, choices=sexo_choices)

    cor_choices = [
        ('Negra', 'Negra'),
        ('Parda', 'Parda'),
        ('Amarela', 'Amarela'),
        ('Indígena', 'Indígena'),
        ('Não informada', 'Não informada')
    ]
    cor = models.CharField(max_length=50, choices=cor_choices)

    idade_choices = [
        ('18 a 59 anos', '18 a 59 anos'),
        ('60 anos ou mais', '60 anos ou mais'),
        ('Sem informação', 'Sem informação')
    ]
    idade = models.CharField(max_length=50, choices=idade_choices)

    vitimas = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.sexo} - {self.cor} - {self.idade}"
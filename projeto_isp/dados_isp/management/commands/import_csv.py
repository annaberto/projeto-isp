from django.core.management.base import BaseCommand
from dados_isp.models import RegistroIncidente
import pandas as pd
from unidecode import unidecode
import chardet


class Command(BaseCommand):
    help = 'Importa dados de um arquivo CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        file_path = 'dados_isp/base_dados/BaseInjuriaPreconceito.csv'
        
        df = pd.read_csv(file_path, encoding='utf-8-sig', sep=';')

        df.columns = [unidecode(col) for col in df.columns]

        mapa_titulos = {
            "Injria por preconceito": "Injúria por preconceito",
            "Preconceito de Raa ou de Cor": "Preconceito de Raça ou de Cor",
            "Preconceito de Raca ou de Cor": "Preconceito de Raça ou de Cor"
        }

        df['Titulo'] = df['Titulo'].apply(lambda x: unidecode(x) if pd.notnull(x) else x)
        df['Titulo'] = df['Titulo'].apply(lambda x: mapa_titulos.get(x, x))

        mapa_sexo = {
            'No informado': 'Não informado',
            'No informada': 'Não informado'
        }

        mapa_cor = {
            'No informada': 'Não informada',
            'No informado': 'Não informada',
            'Indgena': 'Indígena'
        }

        mapa_idade = {
            'Sem informao': 'Sem informação',
        }

        df['Sexo'] = df['Sexo'].apply(lambda x: mapa_sexo.get(unidecode(x), x))
        df['Cor'] = df['Cor'].apply(lambda x: mapa_cor.get(unidecode(x), x))
        df['Idade'] = df['Idade'].apply(lambda x: mapa_idade.get(unidecode(x), x))

        registros = [
            RegistroIncidente(
                cisp=row['Cisp'],
                ano=row['Ano'],
                mes=row['Ms'], 
                titulo=row['Titulo'],
                sexo=row['Sexo'],
                cor=row['Cor'],
                idade=row['Idade'],
                vitimas=row['Vtimas']
            )
            for index, row in df.iterrows()
        ]
        
        RegistroIncidente.objects.bulk_create(registros)

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))

from django.core.management.base import BaseCommand
from dados_isp.models import RegistroIncidente
import pandas as pd
from unidecode import unidecode

class Command(BaseCommand):
    help = 'Importa dados de um arquivo CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        file_path = 'dados_isp/base_dados/BaseInjuriaPreconceito.csv'
        
        df = pd.read_csv(file_path, sep=';', encoding='utf-8-sig')

        print("Antes da normalização:", df.columns)
        
        df.columns = [unidecode(col) for col in df.columns]

        print("Após remoção de acentos:", df.columns)

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

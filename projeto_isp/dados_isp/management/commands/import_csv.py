import pandas as pd
from django.core.management.base import BaseCommand
from dados_isp.models import RegistroIncidente 

class Command(BaseCommand):
    help = 'Importa dados de um arquivo CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        file_path = '/Users/raphaelaberto/Documents/TI/projeto-isp/projeto_isp/base_dados/Base_Injuria_Preconceito (2).csv'

        df = pd.read_csv(file_path, sep=';', encoding='iso-8859-1')

        for index, row in df.iterrows():
            RegistroIncidente.objects.create(
                cisp=row['Cisp'],                          
                ano=row['Ano'],                            
                mes=row['Mês'],                            
                titulo=row['Titulo'],                      
                sexo=row['Sexo'],                          
                cor=row['Cor'],                            
                idade=row['Idade'],                        
                vitimas=row['Vítimas']                     
            )
        
        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))

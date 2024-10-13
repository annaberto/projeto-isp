## Projeto ISP - Importação de Dados de Incidentes de Preconceito

Este projeto tem como objetivo importar, processar e disponibilizar dados de incidentes relacionados a preconceitos de raça ou cor, bem como injúrias por preconceito, a partir de um arquivo CSV. A aplicação é construída utilizando Django como framework web, pandas para manipulação e limpeza de dados, e outras bibliotecas Python para garantir a integridade dos dados e facilitar o processo de importação e visualização.

### Tecnologias Utilizadas

- **Django**: Framework para desenvolvimento web em Python.
- **pandas**: Biblioteca de manipulação de dados em Python.
- **unidecode**: Para remoção de acentos e caracteres especiais.
- **chardet**: Para detecção da codificação do arquivo CSV.

### Estrutura do Projeto

- **dados_isp**: Contém os arquivos de modelos e comandos personalizados.
- **models.py**: Define o modelo `RegistroIncidente` para armazenar os dados no banco de dados.
- **management/commands/import_csv.py**: Comando customizado para importar o arquivo CSV e normalizar os dados.
- **base_dados**: Pasta contendo o arquivo CSV de entrada (`BaseInjuriaPreconceito.csv`).

### Requisitos

Antes de rodar o projeto, certifique-se de que você tenha as seguintes dependências instaladas:

- **Python** >= 3.9
- **Django** >= 4.0
- **pandas**
- **unidecode**
- **chardet**


#### Instalando Dependências

```bash
pip install -r requirements.txt
```


Configuração Inicial
Clone o repositório para sua máquina local:

```bash
git clone https://github.com/annaberto/projeto-isp.git
```

Navegue até o diretório do projeto:

```bash
cd projeto-isp
```

Crie e aplique as migrações do banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

Coloque o arquivo CSV BaseInjuriaPreconceito.csv na pasta dados_isp/base_dados/ do projeto.

Importação de Dados
Para importar os dados do arquivo CSV para o banco de dados, use o comando personalizado:
```
python manage.py import_csv
```
Este comando irá:

- Importar os dados do CSV para a tabela RegistroIncidente no banco de dados.
- Remove acentos e caracteres especiais dos campos do CSV utilizando a biblioteca unidecode.
- Normaliza os valores dos campos Titulo, Sexo, Cor e Idade para garantir consistência e integridade dos dados.

Testando o Projeto
Após importar os dados, você pode iniciar o servidor Django localmente para testar a aplicação:

```
python manage.py runserver
```

Visite http://127.0.0.1:8000 no navegador para acessar a aplicação.

## Banco de Dados

O banco de dados utilizado foi o SQLite3. As tabelas foram criadas utilizando o Django ORM e o SQL gerado está disponível no arquivo `create_database.sql`.

### Estrutura do Banco
O SQL para criação da tabela `registro_incidente` é o seguinte:

```sql
CREATE TABLE "dados_isp_registroincidente" (
    "ano" INTEGER NOT NULL,
    "mes" INTEGER NOT NULL,
    "titulo" TEXT NOT NULL,
    "sexo" TEXT NOT NULL,
    "cor" TEXT NOT NULL,
    "idade" TEXT NOT NULL,
    "vitimas" INTEGER NOT NULL
);
```

## Mapa no QGIS
Além da construção do banco de dados e da aplicação web, foi criada uma visualização geoespacial utilizando o QGIS. A partir do shapefile disponibilizado no site do ISP, referente às Bases Cartográficas Digitais – Circunscrições Integradas de Segurança Pública (CISP) - Limites de 2019, foi gerado um mapa que ajuda a compreender melhor a distribuição espacial dos incidentes.

O mapa foi processado e visualizado no QGIS, permitindo uma análise geográfica mais aprofundada das Circunscrições Integradas de Segurança Pública. Esta visualização é útil para análises espaciais adicionais e complementa a aplicação web com a funcionalidade de CRUD dos dados.

![mapa-cisp-limites-estado](https://github.com/user-attachments/assets/c6ea87d5-f2a6-4376-86f7-1475a5ce053f)

## Authors

<div> 
  <a href="https://www.linkedin.com/in/annaberto" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
  <a href = "https://github.com/annaberto"><img src="https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
  <a href = "mailto:raphaelaberto@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>



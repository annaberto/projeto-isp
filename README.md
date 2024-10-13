## Projeto ISP - Importação de Dados de Incidentes de Preconceito

Este projeto visa importar e normalizar dados de incidentes relacionados a preconceitos de raça ou cor e injúrias por preconceito, disponibilizados em um arquivo CSV, para um banco de dados utilizando **Django** e **pandas**.


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
git clone <URL do repositório>
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
Esse comando irá:
Importar os dados do CSV para a tabela RegistroIncidente no banco de dados.
Remover acentos e caracteres especiais dos campos do CSV utilizando unidecode.
Normalizar os valores dos campos Titulo, Sexo, Cor e Idade para garantir que todos os dados estejam no formato correto.
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

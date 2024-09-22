# Registro de Clientes

Um aplicativo simples para registrar informações de clientes utilizando Python, Tkinter para a interface gráfica e PostgreSQL como banco de dados.

## Funcionalidades

- Cadastro de clientes (nome, email e WhatsApp).
- Listagem de clientes cadastrados.
- Interface gráfica intuitiva.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **Tkinter**: Biblioteca para construção da interface gráfica.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados.
- **psycopg2**: Adaptador para conectar Python ao PostgreSQL.
- **python-dotenv**: Biblioteca para gerenciar variáveis de ambiente.

## Pré-requisitos

Antes de começar, certifique-se de que você tenha o seguinte instalado:

- Python 3.x
- PostgreSQL
- pip (gerenciador de pacotes do Python)


---

# Como usar

## Siga os passos abaixo para criar um ambiente virtual

```
python -m venv .venv
```

---

## Instalando dependências

```
pip install psycopg2 python-dotenv
```

---

## Configurando o Banco de Dados

Crie uma database chamada clientes_db no postgree

```
CREATE DATABASE clientes_db;
```

Crie uma tabela chamada clientes com os seguintes parâmetros

```
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    wapp VARCHAR(15)
);

```

---



### Variáveis de Ambiente

Crie um arquivo chamado config.py na raiz do projeto e adicione suas credenciais de conexão ao banco de dados:

```
DB_NAME="nome_db"
DB_USER="nome_user"
DB_PASSWORD="senha"
DB_HOST="nome_host"

```

Importando as variáveis de ambiente

```
from config importDB_NAME,DB_USER,DB_PASSWORD,DB_HOST
```


---

## Rodando o código - Executando o app

```
python app.py

```

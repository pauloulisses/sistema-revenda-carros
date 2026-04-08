# Sistema de Revenda de Carros

Sistema web desenvolvido com **Django** para gerenciamento de veículos em revendas de carros.
A aplicação permite cadastrar veículos, organizar informações de marcas e realizar buscas por modelo, marca e valor.

## Funcionalidades

* Cadastro de **marcas de veículos**
* Cadastro de **carros**
* Registro de **valor do veículo**
* Busca de carros por **marca**
* Busca por **modelo**
* Filtro de veículos por **preço**
* Gerenciamento através do **Django Admin**

## Tecnologias Utilizadas

* Python
* Django
* SQLite
* HTML5
* CSS3

## Instalação e Execução do Projeto

### 1. Clonar o repositório

git clone https://github.com/seuusuario/sistema-revenda-carros.git

### 2. Acessar a pasta do projeto

cd sistema-revenda-carros

### 3. Criar um ambiente virtual

python -m venv venv

### 4. Ativar o ambiente virtual

**Windows**

venv\Scripts\activate

**Linux / Mac**

source venv/bin/activate

### 5. Instalar as dependências

pip install -r requirements.txt

### 6. Aplicar as migrações do banco de dados

python manage.py migrate

### 7. Executar o servidor de desenvolvimento

python manage.py runserver

Após iniciar o servidor, acesse no navegador:

http://127.0.0.1:8000

## Estrutura do Projeto

sistema-revenda-carros
│
├── cars
│   ├── migrations
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore

## Autor

Paulo Ulisses
Desenvolvedor Backend focado em Python e desenvolvimento de aplicações web com Django.

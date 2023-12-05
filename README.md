# README - Execução do Projeto Django

Este README fornece instruções básicas sobre como configurar e executar um projeto Django usando um ambiente virtual (`venv`) e instalando as dependências listadas no arquivo `requirements.txt`.

## Pré-requisitos

Certifique-se de ter o Python e o pip instalados em sua máquina. Se não tiver, você pode baixá-los em [python.org](https://www.python.org/downloads/) e [pip.pypa.io](https://pip.pypa.io/en/stable/installation/), respectivamente.

## Configuração do Ambiente Virtual

1. Abra um terminal na pasta do seu projeto.

2. Crie um ambiente virtual usando o seguinte comando:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - No MacOS/Linux:

        ```bash
        source venv/bin/activate
        ```

## Instalação das Dependências

1. Com o ambiente virtual ativado, certifique-se de estar na pasta do projeto.

2. Instale as dependências do `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração do Banco de Dados

1. Execute as migrações para criar o banco de dados:

    ```bash
    python manage.py migrate
    ```

2. (Opcional) Crie um superusuário para acessar a interface de administração do Django:

    ```bash
    python manage.py createsuperuser
    ```

## Execução do Projeto

Com todas as dependências instaladas e o banco de dados configurado, você está pronto para iniciar o servidor de desenvolvimento do Django.

```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.

Acesse a interface de administração em `http://127.0.0.1:8000/admin/` (faça login com as credenciais do superusuário, se criado).

Pronto! Seu projeto Django está em execução no ambiente virtual, e você pode começar a desenvolver. Lembre-se de manter o ambiente virtual ativado sempre que estiver trabalhando no projeto.
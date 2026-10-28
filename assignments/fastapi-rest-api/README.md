# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para cadastrar e consultar livros usando FastAPI. Você praticará métodos HTTP, modelos de dados com Pydantic, validação de entrada e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Configure a aplicação FastAPI e crie um endpoint simples para verificar se a API está disponível.

#### Requirements
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Criar uma instância FastAPI chamada `app`.
- Implementar `GET /health`, retornando o JSON `{"status": "ok"}`.
- Permitir iniciar a aplicação com `uvicorn main:app --reload` após renomear `starter-code.py` para `main.py`.
- Disponibilizar a documentação interativa em `/docs`.

### 🛠️ Read and Validate Book Data

#### Description
Defina os modelos de dados dos livros e implemente endpoints para listar o catálogo e consultar um livro pelo identificador.

#### Requirements
O programa concluído deve:

- Definir modelos Pydantic para os dados recebidos e para um livro, com `id`, `title` e `author`.
- Implementar `GET /books` para retornar todos os livros do catálogo.
- Implementar `GET /books/{book_id}` para retornar um livro específico.
- Retornar o status HTTP `404` quando o identificador solicitado não existir.

### 🛠️ Create, Update, and Delete Books

#### Description
Complete o CRUD do catálogo usando os métodos HTTP apropriados. Os dados podem permanecer em memória durante a execução da aplicação.

#### Requirements
O programa concluído deve:

- Implementar `POST /books` para cadastrar um livro e retornar o status `201`.
- Atribuir um identificador único a cada livro criado.
- Implementar `PUT /books/{book_id}` para substituir os dados de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Retornar `404` nas operações de atualização ou remoção quando o livro não existir.
- Informar que os dados armazenados em memória são reiniciados quando a aplicação é encerrada.
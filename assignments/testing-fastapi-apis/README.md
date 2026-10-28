# 📘 Assignment: Testing FastAPI APIs with Pytest

## 🎯 Objective

Crie uma suíte de testes automatizados para a API de livros da atividade Building REST APIs with FastAPI. Você praticará testes de endpoints, validação de respostas HTTP e isolamento do estado entre testes usando `pytest` e `TestClient`.

## 📝 Tasks

### 🛠️ Configure the Test Environment

#### Description
Prepare os arquivos da API e dos testes para que o `pytest` consiga importar a aplicação e enviar requisições sem iniciar um servidor externo.

#### Requirements
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi pytest httpx`.
- Usar a solução da atividade Building REST APIs with FastAPI e renomear o arquivo da aplicação para `main.py`.
- Renomear o arquivo de testes `starter-code.py` para `test_main.py`.
- Criar um cliente de teste com `TestClient(main.app)`.
- Usar uma fixture do `pytest` para restaurar a lista de livros e o próximo ID antes de cada teste.
- Executar os testes com `pytest -q` no diretório que contém `main.py` e `test_main.py`.

### 🛠️ Test Health and Read Endpoints

#### Description
Escreva testes para verificar o endpoint de saúde e as operações que consultam os livros.

#### Requirements
O programa concluído deve:

- Verificar se `GET /health` retorna status `200` e o JSON `{"status": "ok"}`.
- Verificar se `GET /books` retorna status `200` e uma lista de livros com `id`, `title` e `author`.
- Verificar se `GET /books/{book_id}` retorna os dados do livro solicitado.
- Verificar se a consulta a um ID inexistente retorna status `404`.

### 🛠️ Test Create, Update, Delete, and Validation

#### Description
Teste as operações que alteram o catálogo e as respostas para dados inválidos ou recursos inexistentes.

#### Requirements
O programa concluído deve:

- Verificar se `POST /books` cria um livro, retorna status `201` e inclui um ID na resposta.
- Verificar se `PUT /books/{book_id}` atualiza um livro existente e retorna os dados atualizados.
- Verificar se `DELETE /books/{book_id}` remove o livro e se uma consulta posterior retorna `404`.
- Verificar se atualização ou remoção de um ID inexistente retorna `404`.
- Verificar se o envio de dados obrigatórios ausentes retorna status `422`.
- Garantir que a fixture mantenha cada teste independente dos demais.
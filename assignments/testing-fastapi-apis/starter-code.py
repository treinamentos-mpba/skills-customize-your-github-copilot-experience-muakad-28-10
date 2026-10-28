import pytest
from fastapi.testclient import TestClient

import main


client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_books(monkeypatch):
    initial_books = [
        main.Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
        main.Book(id=2, title="Frankenstein", author="Mary Shelley"),
    ]
    monkeypatch.setattr(main, "books", initial_books)
    monkeypatch.setattr(main, "next_book_id", 3)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_books():
    response = client.get("/books")

    assert response.status_code == 200
    # TODO: Verifique a quantidade de livros e os campos de um item.


def test_get_existing_book():
    response = client.get("/books/1")

    assert response.status_code == 200
    # TODO: Verifique os campos e valores do livro retornado.


def test_get_missing_book_returns_404():
    response = client.get("/books/999")

    # TODO: Verifique o status HTTP esperado.
    pass


def test_create_book():
    response = client.post(
        "/books",
        json={"title": "Kindred", "author": "Octavia E. Butler"},
    )

    # TODO: Verifique o status, o ID e os dados do livro criado.
    pass


def test_update_book():
    response = client.put(
        "/books/1",
        json={"title": "The Hobbit: Updated", "author": "J. R. R. Tolkien"},
    )

    # TODO: Verifique o status e os dados atualizados.
    pass


def test_delete_book():
    response = client.delete("/books/1")

    # TODO: Verifique a confirmação e que uma consulta posterior retorna 404.
    pass


def test_invalid_book_data_returns_422():
    response = client.post("/books", json={"title": "Missing author"})

    # TODO: Verifique o status HTTP esperado.
    pass
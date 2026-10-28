from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Frankenstein", author="Mary Shelley"),
]
next_book_id = 3


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Retorne a lista de livros.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Procure o livro pelo ID. Se não existir, lance HTTPException com status 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    global next_book_id

    # TODO: Crie um livro com o próximo ID, adicione-o à lista e retorne-o.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate):
    # TODO: Substitua os dados do livro indicado. Se não existir, lance HTTPException com status 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remova o livro indicado e retorne uma confirmação. Se não existir, lance HTTPException com status 404.
    pass
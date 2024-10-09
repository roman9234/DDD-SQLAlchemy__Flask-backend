from typing import List

from bookstore.app.domain.book import Book
from bookstore.app.infra.storage.book_repository import BookRepository


class MemoryStorage(BookRepository):
    def __init__(self):
        self.books = []

    def add(self, book: Book) -> int:
        self.books.append(book)
        return len(self.books) - 1

    def get(self) -> List[Book]:
        return self.books

    def update(self, id, book: Book):
        self.books[int(id)] = book

    def delete(self, id):
        del self.books[int(id)]

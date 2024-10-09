from abc import ABC, abstractmethod
from typing import List

from bookstore.app.domain.book import Book


class BookRepository(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add(self, book: Book) -> int:
        pass

    @abstractmethod
    def get(self) -> List[Book]:
        pass

    @abstractmethod
    def update(self, id, book: Book):
        pass

    @abstractmethod
    def delete(self, id):
        pass

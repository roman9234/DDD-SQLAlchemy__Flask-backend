import dataclasses
from typing import List

from bookstore.app.domain.book import Book
from bookstore.app.infra.storage.book_repository import BookRepository


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class BookObject(db.Model):
    # __tablename__ = "user_account"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    publish_year = db.Column(db.Integer, nullable=False)
    pages_count = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    def __repr__(self):
        return f"Book(name={self.title!r},id={self.id!r}"


class SqlLiteBookRepository(BookRepository):

    def __init__(self, storage_name: str):
        db.drop_all()
        db.create_all()

    def add(self, book: Book) -> int:
        bo = BookObject(**dataclasses.asdict(book))
        db.session.add(bo)

    def get(self) -> List[Book]:
        books = []
        for x in BookObject.query.order_by(BookObject.id.desc()):
            book = Book(**BookObject.__dict__)
            books.append(book)
        return books

    def update(self, id, book: Book):
        pass

    def delete(self, id: int):
        pass

import dataclasses
import json

from flask import Blueprint, current_app, request

from bookstore.app.context import get_context
from bookstore.app.domain.book import Book

bp = Blueprint("book", __name__)


@bp.get("/")
def get_books():
    ctx = get_context(current_app)

    # Возвращает все books в виде dict ипользуя функцию dataclasses
    return json.dumps([dataclasses.asdict(b) for b in ctx.book_service.get()])


@bp.post("/")
def add_book():
    ctx = get_context(current_app)

    book = Book(**request.json)
    book_id = ctx.book_service.add(book)
    return {"id": book_id, "book": book}

@bp.route("/<id>", methods=["UPDATE"])
def update_book(id):
    ctx = get_context(current_app)

    book = Book(**request.json)
    ctx.book_service.update(id, book)

    return {"id": id, "book": book}


@bp.delete("/<id>")
def delete_book(id):
    ctx = get_context(current_app)

    ctx.book_service.delete(id)

    return {}
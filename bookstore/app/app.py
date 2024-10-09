from flask import Flask
from context import Context
from views.book_controllers import bp as book_bp

from bookstore.app.infra.storage.sqlite_storage import db, SqlLiteBookRepository
from application.book_service import BookService
from infra.storage.mem_storage import MemoryStorage


# Flask предоставляет механизм Blueprint для разделения Handler-ов по разным каталогам
# Он позволяет создавать подмодуль декоратора root, что позволяет описать все пути для Хэндлеров в отдельных файлах

# В этом файле мы определяем приложение Flask, инициализируем контекст

db_name = "test.db"

def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(book_bp, url_prefix="/books")

    # Задаём Config и создаём Instance book_storage, который будем использовать как БД
    _app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_name}'

    db.init_app(_app)
    book_storage = SqlLiteBookRepository(db_name)
    _app.config["CONTEXT"] = Context(book_storage)

    return _app


# def register_extensions(app):
#     db.init_app(app)


app = create_app()
app.run(debug=True)
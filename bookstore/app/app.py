from flask import Flask, g
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

    # Натсройка конфигурации БД
    _app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_name}'
    # Если в поле ниже установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов
    # и посылать сигналы
    # _app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = f'sqlite:///{db_name}'

    # Регистрация Blueprint
    _app.register_blueprint(book_bp, url_prefix="/books")


    # Создаем контекст и добавляем его в app.config
    # book_storage = MemoryStorage()

    # Инициализация БД
    with _app.app_context():
        db.init_app(_app)
    book_storage = SqlLiteBookRepository(db_name)

    # book_storage = MemoryStorage()
    _app.config['CONTEXT'] = Context(book_storage)

    # Добавляем контекст перед каждым запросом
    # @_app.before_request
    # def before_request():
    #     if 'CONTEXT' not in g:
    #         # book_storage = MemoryStorage()
    #         book_storage = SqlLiteBookRepository(db_name)
    #         g.context = Context(book_storage)
    #
    # # Закрываем контект после каждого запроса
    # @_app.teardown_request
    # def teardown_request(exception=None):
    #     g.pop('CONTEXT', None)

    return _app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

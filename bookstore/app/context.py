from application.book_service import BookService
from infra.storage.sqlite_storage import SQLiteStorage

# Контекст - механизм Flask для поддержания состояния приложения в момент его выполнения
# В контексте содержутся все сервисы и зависимости
class Context:
    def __init__(self):
        book_storage = SQLiteStorage("test.db")
        self.book_service = BookService(book_storage)


def get_context(app):
    return app.config["CONTEXT"]
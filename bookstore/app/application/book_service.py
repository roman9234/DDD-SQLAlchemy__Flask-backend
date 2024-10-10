# Проксирует запросы
# Позволяет выбрать ORM для взаимодействия
# ORM должен быть наследником абстрактного класса BookRepository

class BookService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, book):
        # TODO отлов ошибок при добавлении одинаковых книг
        return self.storage.add(book)

    def delete(self, id):
        self.storage.delete(id)

    def get(self):
        return self.storage.get()

    def update(self, id, book):
        self.storage.update(id, book)

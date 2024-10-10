from flask import Flask, g
from context import Context
from views.book_controllers import bp as book_bp

# from bookstore.app.infra.storage.sqlite_storage import db, SqlLiteBookRepository
# from application.book_service import BookService
# from infra.storage.mem_storage import MemoryStorage

# from flask import Flask
# from context import Context
# from views.book import bp as book_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["CONTEXT"] = Context()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

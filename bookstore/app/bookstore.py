from flask import Flask
from context import Context
from views.book import bp as book_bp

def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(book_bp, url_prefix="/books")
    _app.config["CONTEXT"] = Context()

    return _app

app = create_app()
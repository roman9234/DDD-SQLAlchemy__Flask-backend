from sqlite3 import Connection
from flask import g

from bookstore.app.domain.book import Book


class SQLiteConnect(Connection):
    def create_table(self):
        temp_table = '''CREATE TABLE IF NOT EXISTS BOOKS (
            id INTEGER PRIMARY KEY,
            title TEXT,     
            description TEXT,
            publish_year INT,
            pages_count INT,
            created_at DATETIME
        );'''
        self.execute(temp_table)

    def add_row(self, row):
        self.execute("INSERT INTO BOOKS (title, description, publish_year, pages_count, created_at) \
        VALUES (?,?,?,?,?);",
                     (row.title, row.description, row.publish_year,
                      row.pages_count, row.created_at))
        return self.execute(
            "SELECT id FROM BOOKS WHERE title=? AND description=? AND publish_year=? AND pages_count=? AND created_at=?;", \
            (row.title, row.description, row.publish_year, row.pages_count, row.created_at))

    def del_row(self, id):
        temp_del = "DELETE FROM BOOKS WHERE id={};"
        self.execute(temp_del.format(id))

    def get_table(self):
        return self.execute('SELECT * from BOOKS')

    def change_row(self, id, row):
        self.execute("UPDATE BOOKS SET title=?, description=?, publish_year=?, pages_count=?, created_at=? WHERE id=?",
                     (row.title, row.description, row.publish_year,
                      row.pages_count, row.created_at, id))


class SQLiteStorage:
    def __init__(self, database):
        self._database = database
        with SQLiteConnect(self._database) as conn:
            conn.create_table()
            # self.books = SQLiteConnect.create_table('BOOKS')

    def add(self, item):
        with SQLiteConnect(self._database) as conn:
            result = conn.add_row(item)
            res_id = result.fetchall()[0][0]
            return res_id

    def delete(self, id):
        with SQLiteConnect(self._database) as conn:
            conn.del_row(id)

    def get(self):
        with SQLiteConnect(self._database) as conn:
            result = conn.get_table()
            res = result.fetchall()
            return res

    def update(self, id, item):
        with SQLiteConnect(self._database) as conn:
            conn.change_row(id, item)

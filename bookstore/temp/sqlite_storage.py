from sqlite3 import Connection
from flask import g

from domain.book import Book


class SQLiteConnect(Connection):
    def create_table(self):
        temp_table = '''CREATE TABLE IF NOT EXISTS BOOKS (title TEXT,
                     description TEXT,publish_year INT,
                     pages_count INT,created_at DATETIME);'''
        self.execute(temp_table)

    def add_row(self, row):
        self.execute("INSERT INTO BOOKS VALUES (?,?,?,?,?);",
                     (row.title, row.description, row.publish_year,
                      row.pages_count, row.created_at))

    def del_row(self, id):
        temp_del = "DELETE FROM BOOKS WHERE title={};"
        self.execute(temp_del.format(id))

    def get_table(self):
        return self.execute('SELECT * from BOOKS')


class SQLiteStorage:
    def __init__(self, database):
        self._database = database
        with SQLiteConnect(self._database) as conn:
            conn.create_table()
            # self.books = SQLiteConnect.create_table('BOOKS')

    def add(self, item):
        with SQLiteConnect(self._database) as conn:
            conn.add_row(item)

    def delete(self, id):
        with SQLiteConnect(self._database) as conn:
            conn.del_row(id)


    def get(self):
        with SQLiteConnect(self._database) as conn:
            result = conn.get_table()
            return result.fetchmany()

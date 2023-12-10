import sqlite3
import os


class DataBaseHandler:
    def __init__(self, db_path=os.path.abspath("C:\\Users\\Mark\\PycharmProjects\\new_attention_test\\controllers\\at_test.db")):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def register(self, login, password):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO "main"."users" (login, password) VALUES (?, ?)',
                (login, password)
            )
            connection.commit()

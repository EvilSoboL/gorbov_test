import sqlite3
import os


class DataBaseHandler:
    def __init__(self, db_path=os.path.abspath("C:\\Users\\Mark\\PycharmProjects\\new_attention_test\\controllers\\at_test.db")):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def register(self, login, password, is_admin):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            if is_admin:
                cursor.execute(
                    'INSERT INTO "main"."users" (login, password, role) VALUES (?, ?, ?)',
                    (login, password, 1)
                )
            else:
                cursor.execute(
                    'INSERT INTO "main"."users" (login, password, role) VALUES (?, ?, ?)',
                    (login, password, 0)
                )
            connection.commit()

    def login(self, login, password):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT id FROM "main"."users" WHERE login = ? AND password = ?;',
                (login, password)
            )
            result = cursor.fetchone()
            connection.commit()
        return result

    def insert_result(self, user_id, date, first_part, second_part, errors, switching):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO "results" (user_id, date, first_part, second_part, errors)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, date, first_part, second_part, errors, switching))
            connection.commit()

    def get_results(self, user_id):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''
                SELECT * FROM "results" WHERE user_id = ?;
                ''',
                (user_id,)
            )
            result = cursor.fetchall()
            connection.commit()
        return result

#db = DataBaseHandler()
#db.register('ma', 'ma', 0)
import sqlite3
import datetime

class Db:
    def __init__(self, config):
        self.db_name = config.db['name']
    # TODO: when dockerize, create a ccompose field using external sqlite3

    def get_cursor(self):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = lambda column, row: dict(zip([col[0] for col in column.description], row))
        return connection

    def crete_table(self):
        self.get_cursor().execute(
            "CREATE TABLE IF NOT EXISTS {} (id integer primary key AUTOINCREMENT, content char, creationDate date,  author char)".format(
                self.db_name))

    def query(self, query):
        connection = self.get_cursor()
        result = connection.cursor().execute(query)
        connection.commit()
        return result

    def query_and_commit(self, query_type, content, timestamp, author):
        connection = self.get_cursor()
        cursor = connection.cursor()
        query = "{} INTO POSTS VALUES (NULL,?,?, ?)".format(query_type)
        cursor.execute(query, (content, timestamp, author))
        _id = cursor.lastrowid
        self.commit_and_close_connection(connection)
        return {'id': _id}

    def insert(self, content, author):
        timestamp = datetime.datetime.now()
        return self.query_and_commit('INSERT', content, timestamp, author)

    def query_all(self):
        query = 'SELECT * FROM POSTS'
        return self.query(query).fetchall()

    def find_by_id(self, id):
        query = 'SELECT * FROM POSTS WHERE id={}'.format(id)
        results = self.query(query)
        return results.fetchone()

    def edit_post(self, id, content):
        connection = self.get_cursor()
        query = "UPDATE POSTS SET content = ? WHERE id = {}".format(id)
        connection.execute(query, (content,))
        self.commit_and_close_connection(connection)

    def remove_post(self, id):
        query = "DELETE FROM POSTS WHERE id = {}".format(id)
        self.query(query)

    def commit_and_close_connection(self, connection):
        connection.commit()
        connection.close()

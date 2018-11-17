import sqlite3
import datetime


class Db:
    # TODO: serch for retriving object insted of values
    # TODO: when setting up config, watch for more options setting up sqlite3
    # TODO: when dockerize, create a ccompose field using external sqlite3

    def getCursor(self):
        return sqlite3.connect('posts.db')

    def creaeTable(self):
        self.getCursor().execute(
            "CREATE TABLE IF NOT EXISTS Posts (id integer primary key AUTOINCREMENT, content char, creationDate date  author char)")

    def query(self, query):
        connection = self.getCursor()
        result = connection.execute(query)
        return result

    def query_and_commit(self, query_type, content, timestamp, author):
        connection = self.getCursor()
        query = "{} INTO POSTS VALUES (NULL,?,?, ?)".format(query_type)
        connection.execute(query, (content, timestamp, author))
        connection.commit()
        connection.close()
        return

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

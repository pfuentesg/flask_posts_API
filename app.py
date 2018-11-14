from http_instance.Server import app
from Resources.Posts import Posts
from http_instance.api import MainApi
from clients.Db import Db
db= Db()
api = MainApi(app)


def add_resources():
    api.add_source(Posts, '/')


if __name__ == '__main__':
    db.creaeTable()
    add_resources()
    app.run()

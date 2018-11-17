from http_instance.Server import app
from Resources.Posts import Posts, Post
from http_instance.api import MainApi
from clients.Db import Db
db= Db()
api = MainApi(app)


def add_resources():
    api.add_source(Posts, '/')
    api.add_source(Post, '/<int:id>')


if __name__ == '__main__':
    db.creaeTable()
    add_resources()
    app.run()

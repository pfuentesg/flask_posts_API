from Resources.Posts import Posts, Post
from container import db, api, app, config


def add_resources():
    api.add_source(Posts, '/')
    api.add_source(Post, '/<int:id>')


if __name__ == '__main__':
    db.crete_table()
    add_resources()
    app.run(host=config.app['host'], port=config.app['port'])

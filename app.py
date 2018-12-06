from Resources.Posts import Posts, Post
from container import db, api, app, config
from flasgger import Swagger
import os


def add_resources():
    api.add_source(Posts, '/')
    api.add_source(Post, '/<int:id>')


if __name__ == '__main__':
    db.crete_table()
    add_resources()
    swagger = Swagger(app, template_file='../docs/swagger.yml')
    app.run(host=config.app['host'], port=config.app['port'])

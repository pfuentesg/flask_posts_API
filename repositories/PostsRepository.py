from clients.Db import Db

db = Db()


class PostRepository:
    def __init__(self):
        self.db = Db()

    def getOne(self, id):
        return self.db.findById(id)

    def get_all_posts(self):
        return self.db.queryAll()

    def create(self, body):
        content = body['content']
        author = body['author']
        INSERTION = self.db.insert(content, author)
        return INSERTION


    def edit(self):
        return 'edit post from repositories'

    def remove(self):
        return 'remove post from repositories'

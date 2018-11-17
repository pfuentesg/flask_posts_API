from clients.Db import Db

db = Db()


class PostRepository:
    def __init__(self):
        self.db = Db()

    def get_one(self, id):
        return self.db.find_by_id(id)

    def get_all_posts(self):
        return self.db.query_all()

    def create(self, body):
        content = body['content']
        author = body['author']
        INSERTION = self.db.insert(content, author)
        return INSERTION

    def edit(self):
        return 'edit post from repositories'

    def remove(self):
        return 'remove post from repositories'

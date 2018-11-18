from container import Db


class GetOnePost:
    def __init__(self, repo):
        self.repo = repo(Db)

    def execute(self, id):
        post = self.repo.get_one(id)
        if post:
            return post
        else:
            return {'message': 'Post not found'}, 404

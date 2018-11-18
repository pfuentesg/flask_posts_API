from clients.Db import Db


class RemovePost:
    def __init__(self, repo):
        self.repo = repo(Db)

    def execute(self, id):
        return self.repo.remove(id), 204

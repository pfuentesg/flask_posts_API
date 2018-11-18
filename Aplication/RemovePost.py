
class RemovePost:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, id):
        return self.repo.remove(id), 204

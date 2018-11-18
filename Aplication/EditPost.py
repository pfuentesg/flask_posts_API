from container import Db

class EditPost:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, id, data):
        content = data['content']
        self.repo.edit(id, content)
        return '', 204
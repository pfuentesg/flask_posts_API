class RemovePost:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, id):
        response = self.repo.remove(id)
        if str(response) == 'ok':
            return '', 204
        else:
            return 'Error removing post', 500

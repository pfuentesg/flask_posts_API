from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class EditPost:
    def __init__(self):
        self.repo = repo

    def execute(self, id, data):
        content = data['content']
        return self.repo.edit(id, content)

from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class EditPost:
    def __init__(self):
        self.repo = repo

    def execute(self):
        return 'edit post action'

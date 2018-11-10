from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class RemovePost:
    def __init__(self):
        self.repo = repo

    def execute(self):
        return 'Remove post action'

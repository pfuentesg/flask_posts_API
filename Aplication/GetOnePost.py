from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class GetOnePost:
    def __init__(self):
        self.repo = repo

    def execute(self):
        return 'get one post action'

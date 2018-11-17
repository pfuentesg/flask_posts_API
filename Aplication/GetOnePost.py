from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class GetOnePost:
    def __init__(self):
        self.repo = repo

    def execute(self, id):
        return self.repo.get_one(id)

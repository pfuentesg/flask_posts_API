from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class CreatePost:
    def __init__(self):
        self.repo = repo

    def execute(self, body):
        response =  self.repo.create(body)
        return  response

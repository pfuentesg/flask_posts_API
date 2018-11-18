from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class GetOnePost:
    def __init__(self):
        self.repo = repo

    def execute(self, id):
        post = self.repo.get_one(id)
        if post:
            return post
        else:
            return {'message': 'Post not found'}, 404

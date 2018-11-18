from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class GetPosts:
    def __init__(self):
        self.repo = repo

    def execute(self):
        try:
            return self.repo.get_all_posts()

        except:
            'Error'

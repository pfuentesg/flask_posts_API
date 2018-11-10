from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class GetPosts:
    def __init__(self):
        self.repo = repo
        self.responses = {'post_not_found': 'post_not_found'}

    def execute(self):
        try:
            posts = self.repo.getUsers()
            if posts:
                return posts
            else:
                return self.responses['post_not_found']
        except:
            'Error'

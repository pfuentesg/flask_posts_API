from repositories import PostsRepository

repo = PostsRepository.PostRepository()


class CreatePost:
    def __init__(self):
        self.repo = repo

    def execute(self, body):
        try :
            response = self.repo.create(body)
            if response:
                return response, 201
        except Exception as err:
            print('Error creating post', err)
            return 'Error creating post', 500

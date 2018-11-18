from container import Db

class GetPosts:
    def __init__(self, repo):
        self.repo = repo(Db)
        print('init de getPosts')

    def execute(self):
        try:
            return self.repo.get_all_posts()

        except Exception as err:
            print(err)
            return 'Error retriving posts', 500

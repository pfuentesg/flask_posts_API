from Aplication.get_one_post import GetOnePost

test_post = {'id': 'test_id',
             'content': 'test_content',
             'author': 'test_author'}


class Repo:
    def get_one(self, id):
        return test_post

    def __str__(self):
        return 'test_repo'


class RepoReturnsUndefined:
    def get_one(self, id):
        return None


repo = Repo()
repo2 = RepoReturnsUndefined()


def test_get_one():
    getOnePost = GetOnePost(repo)
    assert getOnePost.execute('test_id') == test_post


def test_get_one_return_not_found():
    getOnePost = GetOnePost(repo2)
    assert getOnePost.execute('test_id') == ({'message': 'Post not found'}, 404)

from Aplication.create_post import CreatePost
import pytest

test_post = {'id': 'test_id'}


class Repo:
    def create(self, id):
        return test_post

    def __str__(self):
        return 'test_repo'


class RepoReturnsUndefined:
    def create(self, id):
        return None


repo = Repo()
repo2 = RepoReturnsUndefined()


class TestClass:

    def test_create_one(self):
        createPsot = CreatePost(repo)
        assert createPsot.execute('test_post') == (test_post, 201)

    def test_handling_error(self):
        repo2.create = pytest.raises(BaseException)
        createPsot = CreatePost(repo2)
        assert createPsot.execute('bad_post') == ('Error creating post', 500)

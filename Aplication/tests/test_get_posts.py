from Aplication.get_posts import GetPosts
import pytest
test_post = {'id': 'test_id',
             'content': 'test_content',
             'author': 'test_author'}


class Repo:
    def get_all_posts(self):
        return test_post

    def __str__(self):
        return 'test_repo'


repo = Repo()


class TestClass:

    def test_get_one(self):
        getOnePost = GetPosts(repo)
        assert getOnePost.execute() == test_post


    def test_handling_error(self):
        repo.get_all_posts = pytest.raises(BaseException)
        get_posts = GetPosts(repo)
        assert get_posts.execute() == ('Error retriving posts', 500)

from Aplication.edit_post import EditPost

test_post = {'id': 'test_id'}


class Repo:
    def edit(self, id, content):
        return 'ok'

    def __str__(self):
        return 'test_repo'


class RepoReturnsUndefined:
    def create(self, id):
        return None


repo = Repo()


class TestClass:

    def test_edit(self):
        editPost = EditPost(repo)
        data = {'content': 'fake_data'}
        assert ('', 204) == editPost.execute('fake_id', data)

from Aplication.remove_post import RemovePost

test_post = {'id': 'test_id'}


class Repo:
    def remove(self, id):
        return 'ok'

    def __str__(self):
        return 'test_repo'


def repo_get_All_return_Error(id):
    return 'Errpr'

repo = Repo()


class TestClass:

    def test_edit(self):
        remove_post = RemovePost(repo)
        assert ('', 204) == remove_post.execute('fake_id')

    def test_edite_error_response(self):
        remove_post = RemovePost(repo)
        repo.remove = repo_get_All_return_Error
        assert ('Error removing post', 500) == remove_post.execute('fake_id')

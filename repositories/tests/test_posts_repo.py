from repositories.posts_repository import PostRepository

posts = [{'id': 'test_id',
          'content': 'test_content',
          'author': 'test_author'}
         ]
new_post = {'author': 'test_author', 'content': 'test_content'}


class Db:
    def find_by_id(self, id):
        return posts[0]

    def query_all(self):
        return posts

    def insert(self, content, author):
        return 'fake_id'

    def edit_post(self, id, content):
        return

    def remove_post(self, id):
        return 'ok'

db = Db()
repo = PostRepository(db)

def test_get_posts():
    posts_from_repo = repo.get_all_posts()
    assert posts == posts_from_repo

def test_get_one_post():
    single_post = repo.get_one('fake_id')
    assert posts[0] == single_post

def test_create_post():
    insertion = repo.create(new_post)
    assert 'fake_id' == insertion

def test_edit_post():
    edition = repo.edit('fake_id', new_post['content'])
    assert None == edition

def test_remove_post():
    remove = repo.remove('fake_id')
    assert  'ok' == remove

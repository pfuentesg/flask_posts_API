from flask_restful import Resource
from Aplication import GetPosts, CreatePost, EditPost, GetOnePost, RemovePost

getPosts = GetPosts.GetPosts()
getOnePost = GetOnePost.GetOnePost()
createPosts = CreatePost.CreatePost()
editPost = EditPost.EditPost()
removePost = RemovePost.RemovePost()


class Posts(Resource):
    def __init__(self):
        print('executing posts controller')
        self.getPosts = getPosts
        self.getOnePost = getOnePost
        self.createPosts = createPosts
        self.editPost = editPost
        self.removePost = removePost

    def get(self):
        return self.getPosts.execute()

    def post(self):
        return self.createPosts.execute()

    def patch(self):
        return self.editPost.execute()

    def delete(self):
        return self.removePost.execute()

from flask_restful import Resource, reqparse
from Aplication import GetPosts, CreatePost, EditPost, GetOnePost, RemovePost
from flask import request

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
        responses = getPosts.responses
        res = self.getPosts.execute()

        if res == responses['post_not_found']:
            return 'No posts found', 404
        else:
            return res

    def post(self):
        data = request.get_json(force=True)
        return self.createPosts.execute(data)


class Post(Resource):
    def __init__(self):
        print('executing post controller')
        self.getOnePost = getOnePost
        self.editPost = editPost
        self.removePost = removePost

    def get(self, id):
        res = self.getOnePost.execute(id)
        return res

    def patch(self):
        return self.editPost.execute()

    def delete(self):
        return self.removePost.execute()

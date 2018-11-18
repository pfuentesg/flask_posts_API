from flask_restful import Resource, reqparse
from container import getOnePost, getPosts, createPosts, editPost, removePost
from flask import request


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

    def patch(self, id):
        data = request.get_json(force=True)
        return self.editPost.execute(id, data)

    def delete(self, id):
        return self.removePost.execute(id)

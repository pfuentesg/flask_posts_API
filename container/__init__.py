from clients.Db import Db

db = Db()

from repositories.PostsRepository import PostRepository

postsRepository = PostRepository(db)

from Aplication import GetPosts, CreatePost, EditPost, GetOnePost, RemovePost


getPosts = GetPosts.GetPosts(postsRepository)
getOnePost = GetOnePost.GetOnePost(postsRepository)
createPosts = CreatePost.CreatePost(postsRepository)
editPost = EditPost.EditPost(postsRepository)
removePost = RemovePost.RemovePost(postsRepository)


from http_instance.Server import app
from http_instance.api import MainApi

api = MainApi(app)
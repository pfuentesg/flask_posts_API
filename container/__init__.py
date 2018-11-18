from clients.Db import Db

db = Db()

from Aplication import GetPosts, CreatePost, EditPost, GetOnePost, RemovePost
from repositories.PostsRepository import PostRepository


getPosts = GetPosts.GetPosts(PostRepository)
getOnePost = GetOnePost.GetOnePost(PostRepository)
createPosts = CreatePost.CreatePost(PostRepository)
editPost = EditPost.EditPost(PostRepository)
removePost = RemovePost.RemovePost(PostRepository)

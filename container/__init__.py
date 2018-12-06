# import configuration
import config
config = config
# Import clients
from clients.Db import Db
from logger import logger
db = Db(config)



# Import repositories
from repositories.posts_repository import PostRepository

postsRepository = PostRepository(db)

# Import aplications
from Aplication import get_posts, create_post, edit_post, get_one_post, remove_post

getPosts = get_posts.GetPosts(postsRepository)
getOnePost = get_one_post.GetOnePost(postsRepository)
createPosts = create_post.CreatePost(postsRepository)
editPost = edit_post.EditPost(postsRepository)
removePost = remove_post.RemovePost(postsRepository)

# Import server instance
from http_instance.Server import app
from http_instance.api import MainApi

api = MainApi(app)

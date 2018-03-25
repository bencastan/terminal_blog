from database import Database
from models.post import Post


Database.initialize()

post = Post("Post1 Title", "Post1 Content", "Post1 Author")
post2 = Post("Post2 Title", "Post2 Content", "Post2 Author")


print(post.content)
print(post2.content)


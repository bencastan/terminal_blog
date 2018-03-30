from database import Database
from models.blog import Blog
from models.post import Post

Database.initialize()
blog = Blog(author='Benc',
            title="Sample title",
            description='Sample description')

#post.save_to_mongo()

blog.new_post()

blog.save_to__mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())





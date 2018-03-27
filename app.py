from database import Database
from models.post import Post

Database.initialize()
#post = Post(blog_id="123",
#@            title="Again",
#            content='ahsawpodpsf',
#            author='BenC')

#post.save_to_mongo()


posts = (Post.from_blog('123'))

#print(posts)
for post in posts:
    print(post)


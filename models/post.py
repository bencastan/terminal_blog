import uuid
from database import Database


class Post(object):

    def __init__(self, title, content, author, date, post_id=None):
        self.blog_id = blog.id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if post_id is None else post_id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return{
            'id': self.post_id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
            }

    @staticmethod
    def from_mongo(id):
        # Post.from_mongo(123)
        return Database.find_one(collection='posts', query={'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
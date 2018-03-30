from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for user name
        self.user = input("Enter your author name: ")
        self.user_blog = None
        # Check if they already have an account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            # If not, prompt them to create one
            self._promot_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user}) is not None
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter a blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to__mongo()
        self.user_blog = blog

    def run_menu(self):
        # User read or write a blog?
        read_or_write = input("Do you want to read (R) or wrtie (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blogs()

        # if read:
            # List blogs in DB
            # Allow user to pick one
            # display posts
            pass
        elif read_or_write == 'W':
            self._promopt_write_post()
        # if write
            # check if user has a blog
            # if they do, prompt to write apost
            # if not, prompt to create a new blog
        pass

    def _prompt_write_post(self):
        self.user_blog.new_post()

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})

        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the id fot eh blog you would like ot read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['comment']))

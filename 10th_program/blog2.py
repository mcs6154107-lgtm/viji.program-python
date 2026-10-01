# Blog Management System using Classes

class Post:
    def __init__(self, post_id, title, content):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.comments = []

    def edit(self, title, content):
        self.title = title
        self.content = content

    def add_comment(self, comment):
        self.comments.append(comment)

    def display(self):
        print("\nPost ID:", self.post_id)
        print("Title:", self.title)
        print("Content:", self.content)

        print("Comments:")
        for comment in self.comments:
            print("-", comment)


class Blog:
    def __init__(self):
        self.posts = []
        self.next_id = 1

    def create_post(self, title, content):
        post = Post(self.next_id, title, content)
        self.posts.append(post)
        self.next_id += 1
        print("Post created successfully.")

    def edit_post(self, post_id, title, content):
        for post in self.posts:
            if post.post_id == post_id:
                post.edit(title, content)
                print("Post updated.")
                return

        print("Post not found.")

    def add_comment(self, post_id, comment):
        for post in self.posts:
            if post.post_id == post_id:
                post.add_comment(comment)
                print("Comment added.")
                return

        print("Post not found.")

    def show_posts(self):
        for post in self.posts:
            post.display()


class Admin:
    def moderate(self, blog, post_id, comment):
        for post in blog.posts:
            if post.post_id == post_id:
                if comment in post.comments:
                    post.comments.remove(comment)
                    print("Comment removed.")
                else:
                    print("Comment not found.")
                return

        print("Post not found.")


blog = Blog()
admin = Admin()

blog.create_post(
    "Python Programming",
    "Python is a popular programming language."
)

blog.create_post(
    "Web Development",
    "Python can be used to develop web applications."
)

blog.add_comment(1, "Very useful article!")
blog.add_comment(1, "Great explanation!")

blog.edit_post(
    1,
    "Python Programming Guide",
    "Python is easy to learn and powerful."
)

print("\n----- BLOG POSTS -----")
blog.show_posts()

print("\n----- ADMIN MODERATION -----")
admin.moderate(blog, 1, "Very useful article!")

print("\n----- UPDATED POSTS -----")
blog.show_posts()
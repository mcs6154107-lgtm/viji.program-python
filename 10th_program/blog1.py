# Blog Management System - Basic Python

posts = []
post_id = 1

def create_post():
    global post_id

    title = input("Enter post title: ")
    content = input("Enter post content: ")

    post = {
        "id": post_id,
        "title": title,
        "content": content,
        "comments": []
    }

    posts.append(post)
    post_id += 1

    print("Post created successfully!")


def edit_post():
    pid = int(input("Enter post ID to edit: "))

    for post in posts:
        if post["id"] == pid:
            post["title"] = input("Enter new title: ")
            post["content"] = input("Enter new content: ")
            print("Post updated successfully!")
            return

    print("Post not found.")


def view_posts():
    if not posts:
        print("No posts available.")
        return

    for post in posts:
        print("\nID:", post["id"])
        print("Title:", post["title"])
        print("Content:", post["content"])

        print("Comments:")
        for comment in post["comments"]:
            print("-", comment)


def add_comment():
    pid = int(input("Enter post ID: "))

    for post in posts:
        if post["id"] == pid:
            comment = input("Enter your comment: ")
            post["comments"].append(comment)
            print("Comment added!")
            return

    print("Post not found.")


def moderate_comments():
    pid = int(input("Enter post ID: "))

    for post in posts:
        if post["id"] == pid:
            print("Comments:", post["comments"])

            comment = input("Enter comment to remove: ")

            if comment in post["comments"]:
                post["comments"].remove(comment)
                print("Comment removed by admin.")
            else:
                print("Comment not found.")
            return

    print("Post not found.")


while True:
    print("\n===== BLOG MANAGEMENT SYSTEM =====")
    print("1. Create Post")
    print("2. Edit Post")
    print("3. View Posts")
    print("4. Add Comment")
    print("5. Admin Moderation")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_post()
    elif choice == "2":
        edit_post()
    elif choice == "3":
        view_posts()
    elif choice == "4":
        add_comment()
    elif choice == "5":
        moderate_comments()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
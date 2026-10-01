# Library Management System - Basic Python

books = []
book_id = 1


def add_book():
    global book_id

    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    book_id += 1

    print("Book added successfully!")


def issue_book():
    bid = int(input("Enter book ID to issue: "))

    for book in books:
        if book["id"] == bid:

            if book["issued"]:
                print("Book is already issued.")
            else:
                book["issued"] = True
                print("Book issued successfully.")

            return

    print("Book not found.")


def return_book():
    bid = int(input("Enter book ID to return: "))

    for book in books:
        if book["id"] == bid:

            if book["issued"]:
                book["issued"] = False
                print("Book returned successfully.")
            else:
                print("Book was not issued.")

            return

    print("Book not found.")


def view_books():
    if not books:
        print("No books available.")
        return

    for book in books:
        print("\nID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])

        if book["issued"]:
            print("Status: Issued")
        else:
            print("Status: Available")


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        view_books()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
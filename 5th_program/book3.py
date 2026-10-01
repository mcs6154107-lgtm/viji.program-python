class Book:
    def __init__(self, name):
        self.name = name
        self.issued = False


class User:
    def __init__(self, name):
        self.name = name

    def issue(self, book):
        if not book.issued:
            book.issued = True
            print(self.name, "issued", book.name)
        else:
            print(book.name, "is already issued.")

    def return_book(self, book):
        book.issued = False
        print(self.name, "returned", book.name)


class Student(User):
    def issue(self, book):
        print("Student:")
        super().issue(book)


class Faculty(User):
    def issue(self, book):
        print("Faculty:")
        super().issue(book)


class Guest(User):
    def issue(self, book):
        print("Guest:")
        super().issue(book)


book = Book("Object Oriented Programming")

users = [
    Student("Kiran"),
    Faculty("Anitha"),
    Guest("Vijay")
]

for user in users:
    user.issue(book)
    if book.issued:
        user.return_book(book)
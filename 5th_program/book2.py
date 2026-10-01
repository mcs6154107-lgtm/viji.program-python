class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def get_status(self):
        return "Available" if self.available else "Issued"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def user_type(self):
        return "General User"


class Student(User):
    def user_type(self):
        return "Student"


class Faculty(User):
    def user_type(self):
        return "Faculty"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def issue_book(self, user, book):
        if book.available:
            book.available = False
            print(f"{user.name} ({user.user_type()}) issued {book.title}")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, user, book):
        book.available = True
        print(f"{user.name} returned {book.title}")

    def show_books(self):
        for book in self.books:
            print(book.book_id, book.title, book.get_status())


library = Library()

book1 = Book(101, "Data Structures")
book2 = Book(102, "Java Programming")

student = Student(1, "Arun")
faculty = Faculty(2, "Meena")

library.add_book(book1)
library.add_book(book2)

library.add_user(student)
library.add_user(faculty)

library.issue_book(student, book1)
library.issue_book(faculty, book2)

library.show_books()

library.return_book(student, book1)
library.show_books()
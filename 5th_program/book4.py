class Book:
    def __init__(self, title):
        self.title = title
        self.issued_to = None

    def is_available(self):
        return self.issued_to is None


class User:
    limit = 1

    def __init__(self, name):
        self.name = name
        self.books = []

    def can_borrow(self):
        return len(self.books) < self.limit

    def issue_book(self, book):
        if not book.is_available():
            print("Book is already issued.")
        elif not self.can_borrow():
            print(self.name, "cannot borrow more books.")
        else:
            book.issued_to = self
            self.books.append(book)
            print(self.name, "issued", book.title)

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.issued_to = None
            print(self.name, "returned", book.title)


class Student(User):
    limit = 2


class Teacher(User):
    limit = 5


book1 = Book("C Programming")
book2 = Book("Python")
book3 = Book("Java")

student = Student("Ravi")
teacher = Teacher("Lakshmi")

student.issue_book(book1)
student.issue_book(book2)
student.issue_book(book3)

teacher.issue_book(book3)

student.return_book(book1)
teacher.issue_book(book1)
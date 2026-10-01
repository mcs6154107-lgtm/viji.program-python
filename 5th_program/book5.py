from abc import ABC, abstractmethod


class LibraryUser(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def borrow_limit(self):
        pass

    def issue_book(self, book):
        if book.available and self.borrow_limit() > 0:
            book.available = False
            print(self.name, "issued", book.title)
        else:
            print("Cannot issue", book.title)

    def return_book(self, book):
        book.available = True
        print(self.name, "returned", book.title)


class Student(LibraryUser):
    def borrow_limit(self):
        return 3


class Teacher(LibraryUser):
    def borrow_limit(self):
        return 10


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.title} - {self.author} - {status}")


book = Book("Machine Learning", "Tom Mitchell")

student = Student("Amit")
teacher = Teacher("Suresh")

book.display()

student.issue_book(book)
book.display()

student.return_book(book)
book.display()

teacher.issue_book(book)
book.display()
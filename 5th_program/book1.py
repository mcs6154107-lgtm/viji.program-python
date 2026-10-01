class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        status = "Issued" if self.issued else "Available"
        print(f"{self.title} by {self.author} - {status}")


class User:
    def __init__(self, name):
        self.name = name

    def issue_book(self, book):
        if not book.issued:
            book.issued = True
            print(f"{self.name} issued '{book.title}'")
        else:
            print(f"'{book.title}' is already issued.")

    def return_book(self, book):
        if book.issued:
            book.issued = False
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"'{book.title}' was not issued.")


class Student(User):
    def issue_book(self, book):
        print("Student issuing book:")
        super().issue_book(book)


class Teacher(User):
    def issue_book(self, book):
        print("Teacher issuing book:")
        super().issue_book(book)


book1 = Book("Python Programming", "Guido van Rossum")

student = Student("Rahul")
teacher = Teacher("Priya")

student.issue_book(book1)
book1.display()

student.return_book(book1)
book1.display()

teacher.issue_book(book1)
book1.display()
# Student Management System - Basic Python

students = []
student_id = 1


def add_student():
    global student_id

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    student_id += 1

    print("Student added successfully!")


def edit_student():
    sid = int(input("Enter student ID to edit: "))

    for student in students:

        if student["id"] == sid:

            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["course"] = input("Enter new course: ")

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    sid = int(input("Enter student ID to delete: "))

    for student in students:

        if student["id"] == sid:

            students.remove(student)

            print("Student deleted successfully!")
            return

    print("Student not found.")


def view_students():
    if not students:
        print("No students available.")
        return

    for student in students:

        print("\nID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Edit Student")
    print("3. Delete Student")
    print("4. View Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        edit_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        view_students()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
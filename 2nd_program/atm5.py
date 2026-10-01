marks = 0

while True:
    print("\n===== STUDENT MENU =====")
    print("1. Enter Marks")
    print("2. Show Grade")
    print("3. Check Pass/Fail")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        marks = float(input("Enter your marks: "))

        if marks >= 0 and marks <= 100:
            print("Marks entered successfully")
        else:
            print("Invalid marks")

    elif choice == 2:
        if marks >= 90:
            print("Grade: A")
        elif marks >= 75:
            print("Grade: B")
        elif marks >= 60:
            print("Grade: C")
        elif marks >= 40:
            print("Grade: D")
        else:
            print("Grade: F")

    elif choice == 3:
        if marks >= 40:
            print("Student Passed")
        else:
            print("Student Failed")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")

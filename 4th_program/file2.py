import json

FILE = "contacts.json"


def read_file():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def write_file(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_contact(data):
    contact = {}

    contact["name"] = input("Name: ")
    contact["phone"] = input("Phone: ")
    contact["email"] = input("Email: ")

    data.append(contact)
    write_file(data)

    print("Added successfully.")


def search_contact(data):
    search = input("Enter name: ").lower()

    found = False

    for contact in data:
        if search in contact["name"].lower():
            print("\nName:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("No contact found.")


def delete_contact(data):
    phone = input("Enter phone number: ")

    for contact in data:
        if contact["phone"] == phone:
            data.remove(contact)
            write_file(data)
            print("Deleted successfully.")
            return

    print("Contact not found.")


def show_contacts(data):
    if len(data) == 0:
        print("No contacts available.")
        return

    for i, contact in enumerate(data, 1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


contacts = read_file()

while True:

    print("\n===== MENU =====")
    print("1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        search_contact(contacts)

    elif choice == "3":
        delete_contact(contacts)

    elif choice == "4":
        show_contacts(contacts)

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

import json
import os

FILE = "contacts.json"


def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


contacts = load_data()

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        phone = input("Enter phone: ")

        if phone in contacts:
            print("Contact already exists.")
        else:
            name = input("Enter name: ")
            email = input("Enter email: ")

            contacts[phone] = {
                "name": name,
                "email": email
            }

            save_data(contacts)
            print("Contact added.")

    elif choice == "2":

        phone = input("Enter phone: ")

        if phone in contacts:
            print("Name:", contacts[phone]["name"])
            print("Phone:", phone)
            print("Email:", contacts[phone]["email"])
        else:
            print("Contact not found.")

    elif choice == "3":

        phone = input("Enter phone: ")

        if phone in contacts:
            del contacts[phone]
            save_data(contacts)
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":

        if not contacts:
            print("No contacts.")

        for phone, details in contacts.items():
            print("\nName:", details["name"])
            print("Phone:", phone)
            print("Email:", details["email"])

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

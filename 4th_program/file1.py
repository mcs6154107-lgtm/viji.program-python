import json
import os

FILE = "contacts.json"


def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)


contacts = load_contacts()

while True:
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        save_contacts(contacts)
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ").lower()

        for contact in contacts:
            if name in contact["name"].lower():
                print(contact)

    elif choice == "3":
        phone = input("Enter phone number to delete: ")

        for contact in contacts:
            if contact["phone"] == phone:
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted.")
                break
        else:
            print("Contact not found.")

    elif choice == "4":
        for contact in contacts:
            print(contact)

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

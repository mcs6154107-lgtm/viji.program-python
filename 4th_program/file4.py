import json

FILE = "contacts.json"


def load_contacts():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts():
    with open(FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts()
    print("Contact added successfully.")


def search_contact():
    name = input("Enter name to search: ").lower()

    for c in contacts:
        if c["name"].lower() == name:
            print("\nContact Found")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            return

    print("Contact not found.")


def update_contact():
    phone = input("Enter phone number: ")

    for c in contacts:

        if c["phone"] == phone:

            print("Leave blank to keep old value.")

            name = input("New name: ")
            email = input("New email: ")

            if name:
                c["name"] = name

            if email:
                c["email"] = email

            save_contacts()

            print("Contact updated.")
            return

    print("Contact not found.")


def delete_contact():
    phone = input("Enter phone number: ")

    for c in contacts:

        if c["phone"] == phone:
            contacts.remove(c)
            save_contacts()

            print("Contact deleted.")
            return

    print("Contact not found.")


def display_contacts():

    if not contacts:
        print("No contacts available.")
        return

    for c in contacts:
        print("----------------")
        print("Name:", c["name"])
        print("Phone:", c["phone"])
        print("Email:", c["email"])


contacts = load_contacts()

while True:

    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Display")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        display_contacts()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
        
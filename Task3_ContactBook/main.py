import json
import os

# File to store contacts
FILE = "contacts.json"

# Load contacts from file or return empty dict
def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"{name}'s contact added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts saved yet.")
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")

# Search contact
def search_contact(contacts):
    keyword = input("Search by name or phone: ").lower()
    found = False
    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("No contact found.")

# Update existing contact
def update_contact(contacts):
    name = input("Enter name to update: ")
    if name in contacts:
        print("Leave blank to keep existing value.")
        phone = input(f"New phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email ({contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address ({contacts[name]['address']}): ") or contacts[name]['address']

        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"{name}'s contact updated.")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name}'s contact deleted.")
    else:
        print("Contact not found.")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

"""
task_04: 
Description: A command-line contact book that stores contacts as a list of dictionaries 
             and allows the user to add, search, view, and delete contacts.
"""

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

def view_all():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact Book ---")
        print(f"{'Name':<15} | {'Phone':<15} | {'Email':<25}")
        print("-" * 60)
        for contact in contacts:
            print(f"{contact['name']:<15} | {contact['phone']:<15} | {contact['email']:<25}")

while True:
    print("\n--- Contact Book Menu ---")
    print("1 = Add")
    print("2 = Search")
    print("3 = Delete")
    print("4 = View All")
    print("5 = Exit")
    
    choice = input("Choose an action (1-5): ").strip()
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter name to search: ")
        result = search_contact(name)
        if result:
            print(f"Found: Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}")
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("Exiting contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

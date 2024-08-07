contacts = {}

def display_menu():
    print("")
    print("Contact Book Menu")
    print("1. Add a New Contact")
    print("2. View All Contacts")
    print("3. Update a Contact")
    print("4. Delete a Contact")
    print("5. Exit")
    print("")

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        for name, details in contacts.items():
            print("")
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()



def display_menu():
    """Display the menu for the contact management system."""
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    """Add a new contact to the contact list."""
    print("\nAdd New Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts(contacts):
    """Display all contacts in the contact list."""
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
    else:
        print("\nNo contacts available.")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    print("\nSearch Contact")
    search_term = input("Enter name or phone number to search: ")
    
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-----------------------------")
    else:
        print("No contacts found.")

def update_contact(contacts):
    """Update the details of an existing contact."""
    print("\nUpdate Contact")
    name = input("Enter the name of the contact to update: ")
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Contact found. Enter new details.")
            contact['phone'] = input("Enter New Phone Number: ")
            contact['email'] = input("Enter New Email: ")
            contact['address'] = input("Enter New Address: ")
            print("Contact updated successfully!")
            return
    
    print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact from the contact list."""
    print("\nDelete Contact")
    name = input("Enter the name of the contact to delete: ")
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    
    print("Contact not found.")

def main():
    contacts = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

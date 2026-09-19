contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully.")
    
    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\n--- ALL CONTACTS ---")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully.")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice.")

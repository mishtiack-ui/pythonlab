contacts = []
while True:
print("\n--- CONTACT BOOK ---")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Delete Contact")
print("5. Exit")
choice = input("Enter your choice: ")
# Add contact
if choice == "1":
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
contact = {
"name": name,
"phone": phone,
"email": email
}
contacts.append(contact)
print("Contact added successfully.")
# View contacts
elif choice == "2":
if len(contacts) == 0:
print("No contacts available.")
else:
print("\n--- ALL CONTACTS ---")
for contact in contacts:
print("Name:", contact["name"])
contacts = []
while True:
print("\n--- CONTACT BOOK ---")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Delete Contact")
print("5. Exit")
choice = input("Enter your choice: ")
# Add contact
if choice == "1":
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
contact = {
"name": name,
"phone": phone,
"email": email
}
contacts.append(contact)
print("Contact added successfully.")
# View contacts
elif choice == "2":
if len(contacts) == 0:
print("No contacts available.")
else:
print("\n--- ALL CONTACTS ---")
for contact in contacts:
print("Name:", contact["name"])
print("Exiting Contact Book...")
break
else:
print("Invalid choice.")

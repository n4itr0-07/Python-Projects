contacts = {}

while True:
    print("\nWelcome to Contact Book")
    print("📑--------------------------📑")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        if name in contacts:
            print(f"Contact name: {name} already exists!")
        else:
            age = input("Enter age: ")
            mobile = input("Enter phone number: ")
            email = input("Enter email address: ")
            contacts[name] = {'age': int(age), 'mobile': mobile, 'email': email}
            print(f"Contact added successfully: {name}")

    elif choice == '2':
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Mobile Number: {contact['mobile']}, Email: {contact['email']}")
        else:
            print(f"Contact name: {name} not found!")
        print("-------------------")

    elif choice == '3':
        name = input("Enter contact name to update: ")
        if name in contacts:
            age = input("Enter new age: ")
            mobile = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contacts[name] = {'age': int(age), 'mobile': mobile, 'email': email}
            print(f"Contact updated successfully: {name}")
        else:
            print(f"Contact name: {name} not found!")

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact deleted successfully: {name}")
        else:
            print(f"Contact name: {name} not found!")

    elif choice == '5':
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age: {contact['age']}, Mobile Number: {contact['mobile']}, Email: {contact['email']}")
                found = True
        
        if not found:
            print(f"Contact name: {search_name} not found!")

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    elif choice == '7':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

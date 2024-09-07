# Contact Book

A simple command-line application to manage contacts. The Contact Book allows users to create, view, update, delete, search, and count contacts. This guide provides step-by-step instructions to help you understand the functionality and features of the program.

## Features

1. **Create Contact**: Add a new contact with details such as name, age, mobile number, and email.
2. **View Contact**: View the details of an existing contact by name.
3. **Update Contact**: Update the details of an existing contact.
4. **Delete Contact**: Remove a contact from the contact book.
5. **Search Contact**: Search for a contact by name.
6. **Count Contacts**: Display the total number of contacts.
7. **Exit**: Exit the application.

## Usage

### Step-by-step Guide

1. **Initialize the Contact Book**
   - The `contacts` dictionary is initialized to store all contact details.
   - A `while True` loop is used to keep the program running until the user chooses to exit.

2. **Display the Menu**
   - A menu is displayed with options (1-7) to interact with the Contact Book:
     ```python
     print("\nWelcome to Contact Book")
     print("📑--------------------------📑")
     print("1. Create Contact")
     print("2. View Contact")
     print("3. Update Contact")
     print("4. Delete Contact")
     print("5. Search Contact")
     print("6. Count Contacts")
     print("7. Exit")
     ```
   - The user is prompted to enter their choice using `input`.

3. **Create a Contact**
   - If the user selects **1**:
     - Prompt the user for contact details: `name`, `age`, `mobile`, and `email`.
     - If the `name` already exists in `contacts`, display a message; otherwise, add the new contact to the `contacts` dictionary.
     - Display a success message.

4. **View a Contact**
   - If the user selects **2**:
     - Prompt the user for the contact `name` to view.
     - Check if the `name` exists in `contacts`. If it does, display the contact's details; otherwise, show a "not found" message.

5. **Update a Contact**
   - If the user selects **3**:
     - Prompt the user for the `name` of the contact to update.
     - If the `name` exists, ask for new details: `age`, `mobile`, and `email`.
     - Update the contact information in the `contacts` dictionary and display a success message.

6. **Delete a Contact**
   - If the user selects **4**:
     - Prompt the user for the `name` of the contact to delete.
     - If the `name` exists, delete it from the `contacts` dictionary and display a success message.

7. **Search for a Contact**
   - If the user selects **5**:
     - Prompt the user for the `search_name` to search.
     - Loop through the `contacts` dictionary to find matches (case insensitive).
     - Display the found contact(s) or show a "not found" message.

8. **Count Contacts**
   - If the user selects **6**:
     - Display the total number of contacts using `len(contacts)`.

9. **Exit the Program**
   - If the user selects **7**:
     - Print "Exiting..." and break out of the loop to end the program.

10. **Handle Invalid Input**
    - If the user enters an invalid choice, display an "Invalid choice" message.

### Sample Output

```
Welcome to Contact Book
📑--------------------------📑
1. Create Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. Search Contact
6. Count Contacts
7. Exit
Enter your choice: 1
Enter name: John Doe
Enter age: 30
Enter phone number: 1234567890
Enter email address: john.doe@example.com
Contact added successfully: John Doe
```

## Getting Started

To use this Contact Book:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Salik-Seraj/Python-Projects
   cd Project 11
   ```

2. **Run the Program**:
   ```bash
   python contact_book.py
   ```

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

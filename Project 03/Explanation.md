# File Management Application Guide

This guide provides a step-by-step walkthrough for creating a simple file management application in Python. The application allows users to create, view, delete, search, read, and edit files in a directory.

## Step 1: Clone the GitHub Repository

First, clone the repository to your local machine. Replace `your-repo-link` with your actual repository link.

```bash
git clone https://github.com/Salik-Seraj/Python-Projects.git

cd your-repo-directory
```

## Step 2: Create the Python Script

Create a new Python file, `file_management.py`, and add the following code:

```python
import os

def create_file(filename):
    try:
        with open(filename, 'x') as file:
            pass
        print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except Exception as e:
        print(f"Error creating file '{filename}': {str(e)}")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found.")
    else:
        print("Files In Directory !")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error deleting file '{filename}': {str(e)}")

def search_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"File '{filename}':")
            print(contents)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file '{filename}': {str(e)}")

def read_file(filename):
    try:
        with open("sample.txt", 'r') as file:
            content = file.read()
            print(f"File '{filename}' :\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file '{filename}': {str(e)}")

def edit_file(filename):
    try:
        with open("sample.txt", 'a') as file:
            content = input("Enter data to add : ")
            file.write(content + "\n")
            print(f"Content added to '{filename}' Successfully")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error editing file '{filename}': {str(e)}")

def main():
    while True:
        print("🔥 FILE MANAGEMENT APP 🔥 ")
        print("\nChoose an option : ")
        print("1. Create a new file ")
        print("2. View all files ")
        print("3. Delete a file ")
        print("4. Search a file ")
        print("5. Read a file ")
        print("6. Edit a file ")
        print("7. Exit🆘")

        choice = int(input("Enter your choice :--> "))
        
        if choice == 1:
            filename = input("Enter file name :--> ")
            create_file(filename)
        elif choice == 2:
            view_all_files()
        elif choice == 3:
            filename = input("Enter file name to delete :--> ")
            delete_file(filename)
        elif choice == 4:
            filename = input("Enter file name to search :--> ")
            search_file(filename)
        elif choice == 5:
            filename = input("Enter file name to read :--> ")
            read_file(filename)
        elif choice == 6:
            filename = input("Enter file name to edit :--> ")
            edit_file(filename)
        elif choice == 7:
            print("Exiting the application...")
            break
        else:
            print("Invalid option 😁. Please try again.")

if __name__ == "__main__":
    main()
```

## Step 3: Run the Application

To run the application, execute the following command in your terminal:

```bash
python file_management.py
```

## Step 4: Use the Application

### Create a New File

1. Select option `1` from the menu.
2. Enter the desired file name.

### View All Files

1. Select option `2` from the menu.

### Delete a File

1. Select option `3` from the menu.
2. Enter the name of the file you want to delete.

### Search a File

1. Select option `4` from the menu.
2. Enter the name of the file you want to search.

### Read a File

1. Select option `5` from the menu.
2. Enter the name of the file you want to read.

### Edit a File

1. Select option `6` from the menu.
2. Enter the name of the file you want to edit.
3. Enter the content you want to add to the file.

### Exit the Application

1. Select option `7` from the menu.

That's it! You've successfully created and run a simple file management application in Python.


## Follow Me

If you found this guide helpful, follow me for more tutorials and projects on GitHub and other social media platforms!

- [GitHub](https://github.com/Salik-Seraj)
- [X](https://twitter.com/code_with_ssn)
- [LinkedIn](https://linkedin.com/in/salik-seraj-naik)
- [Personal Website](https://linktr.ee/SalikSerajNaik)
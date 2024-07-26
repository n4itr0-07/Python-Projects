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
            # print(content)

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
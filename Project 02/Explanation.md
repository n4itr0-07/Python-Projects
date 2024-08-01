# Student Grades Management System

This project is a simple command-line application for managing student grades. You can add, update, delete, and view student grades using this application.

## Features

1. Add a new student and grade.
2. Update an existing student's grade.
3. Delete a student.
4. View all students and their grades.

## Code

```python
# Initialising dictionary
student_grades = {}

# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' added with grade '{grade}' successfully.")

# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Grade for student '{name}' updated to '{grade}'.")
    else:
        print(f"Student '{name}' not found.")

# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student '{name}' deleted successfully.")
    else:
        print(f"Student '{name}' not found.")

# View all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("\nChoose an operation:")
        print("1. Add a student")
        print("2. Update a student's grade")
        print("3. Delete a student")
        print("4. View all students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student's name: ")
            grade = input("Enter student's grade: ")
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student's name: ")
            grade = input("Enter new grade: ")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student's name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

main()
```

## Step-by-Step Guide

### 1. Initializing the Dictionary
First, we initialize an empty dictionary `student_grades` to store the names and grades of students.

```python
student_grades = {}
```

### 2. Adding a New Student
The `add_student` function takes a student's name and grade as inputs and adds them to the `student_grades` dictionary.

```python
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' added with grade '{grade}' successfully.")
```

### 3. Updating a Student's Grade
The `update_student` function updates the grade for an existing student. If the student is not found, it prints a message indicating so.

```python
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Grade for student '{name}' updated to '{grade}'.")
    else:
        print(f"Student '{name}' not found.")
```

### 4. Deleting a Student
The `delete_student` function removes a student from the `student_grades` dictionary. If the student is not found, it prints a message indicating so.

```python
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student '{name}' deleted successfully.")
    else:
        print(f"Student '{name}' not found.")
```

### 5. Viewing All Students
The `display_all_students` function prints all the students and their grades. If there are no students, it prints a message indicating so.

```python
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")
```

### 6. Main Function
The `main` function provides a menu for the user to interact with the application. It allows the user to choose an operation: add, update, delete, view, or exit.

```python
def main():
    while True:
        print("\nStudent Grades Management System")
        print("\nChoose an operation:")
        print("1. Add a student")
        print("2. Update a student's grade")
        print("3. Delete a student")
        print("4. View all students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student's name: ")
            grade = input("Enter student's grade: ")
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student's name: ")
            grade = input("Enter new grade: ")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student's name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

main()
```

### Running the Program
To run the program, simply execute the Python script. You will be presented with a menu where you can choose the desired operation by entering the corresponding number.

```sh
python student_grades_management.py
```

That's it! You now have a functional Student Grades Management System. Feel free to modify and expand the code to add more features as needed.

## Follow Me

If you found this guide helpful, follow me for more tutorials and projects on GitHub and other social media platforms!

- [GitHub](https://github.com/Salik-Seraj)
- [X](https://twitter.com/code_with_ssn)
- [LinkedIn](https://linkedin.com/in/salik-seraj-naik)
- [Personal Website](https://linktr.ee/SalikSerajNaik)
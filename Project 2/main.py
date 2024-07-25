
# Initialising dictionary
student_grades = { }

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
        # print("All students:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")


def main():
    while True:
        print("\n Student Grades Managment System")
        print("\nChoose an operation:")
        print("1. Add a student")
        print("2. Update a student's grade")
        print("3. Delete a student")
        print("4. View all students")
        print("5. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            name = input("Enter student's name : ")
            grade = input("Enter student's grade : ")
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student's name : ")
            grade = input("Enter new grade : ")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student's name : ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

main()


from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database

# Functions
# def update_employee():
#     # Placeholder function for updating employee details
#     selected_item = tree.selection()
#     if not selected_item:
#         messagebox.showerror("Error", "No employee selected.")

#     else:
#         database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
#         treeview_data()
#         clear()
#         messagebox.showinfo("Success","Data is updated successfully")
def update_employee():
    # Placeholder function for updating employee details
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No employee selected.")
    else:
        try:
            # Debugging: Print selected item
            print(f"Selected item: {selected_item}")

            # Assuming 'idEntry' contains the ID of the selected employee
            id_value = idEntry.get()
            name_value = nameEntry.get()
            phone_value = phoneEntry.get()
            role_value = roleBox.get()
            gender_value = genderBox.get()
            salary_value = salaryEntry.get()

            # Debugging: Print retrieved values
            print(f"Updating ID: {id_value}")
            print(f"Name: {name_value}, Phone: {phone_value}, Role: {role_value}, Gender: {gender_value}, Salary: {salary_value}")

            # Update the database
            database.update(id_value, name_value, phone_value, role_value, gender_value, salary_value)
            
            # Refresh the tree view with updated data
            treeview_data()

            # Clear the entry fields
            clear()

            # Show success message
            messagebox.showinfo("Success", "Data is updated successfully")

        except Exception as e:
            # Debugging: Print the exception
            print(f"Error occurred: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")

# Make sure to define the `treeview_data` and `clear` functions as well



def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)["values"]
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])


def clear ():
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set("Penetration Tester")
    genderBox.set("Male")
    salaryEntry.delete(0, END)


def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())  # Clear the treeview before adding new data
    for employee in employees:
        tree.insert('', END, values=employee)
# def treeview_data():
#     # Clear the current data
#     for item in tree.get_children():
#         tree.delete(item)
#     # Fetch updated data from the database
#     mycourser.execute("SELECT * FROM data")
#     rows = mycourser.fetchall()
#     # Insert updated data into the tree view
#     for row in rows:
#         tree.insert("", "end", values=row)



def add_employee():
    if idEntry.get() == "" or phoneEntry.get() == "" or nameEntry.get() == "" or salaryEntry.get() == "":
        messagebox.showerror("Error", "Please enter all fields.")
    else:
        database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        clear()
        treeview_data()  # Refresh the treeview
        messagebox.showinfo("Success", "Data saved successfully")


def delete_employee():
    selected_item = tree.selection()[0]
    tree.delete(selected_item)
    # Implement database deletion logic here

def delete_all_employees():
    for item in tree.get_children():
        tree.delete(item)
    # Implement database deletion logic here

window = CTk()
window.geometry("930x580")
window.resizable(False, False)
window.title("Employee Management System")
window.configure(fg_color="#161C30")

# Logo
logo = CTkImage(Image.open("Images/header.jpeg"), size=(930, 158))
logoLabel = CTkLabel(window, image=logo, text="")
logoLabel.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Left Frame
leftFrame = CTkFrame(window, fg_color="#161C30")
leftFrame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

# ID Label
idLabel = CTkLabel(leftFrame, text="Id", font=("arial", 18, "bold"), text_color="white")
idLabel.grid(row=0, column=0, padx=20, pady=10, sticky="w")

idEntry = CTkEntry(leftFrame, font=("arial", 15, "bold"), width=180)
idEntry.grid(row=0, column=1)

# Name Label
nameLabel = CTkLabel(leftFrame, text="Name", font=("arial", 18, "bold"), text_color="white")
nameLabel.grid(row=1, column=0, padx=20, pady=10, sticky="w")

nameEntry = CTkEntry(leftFrame, font=("arial", 15, "bold"), width=180)
nameEntry.grid(row=1, column=1)

# Phone Label
phoneLabel = CTkLabel(leftFrame, text="Phone", font=("arial", 18, "bold"), text_color="white")
phoneLabel.grid(row=2, column=0, padx=20, pady=10, sticky="w")

phoneEntry = CTkEntry(leftFrame, font=("arial", 15, "bold"), width=180)
phoneEntry.grid(row=2, column=1)

# Role Label
roleLabel = CTkLabel(leftFrame, text="Role", font=("arial", 18, "bold"), text_color="white")
roleLabel.grid(row=3, column=0, padx=20, pady=10, sticky="w")

role_options = ["Security Architect", "Penetration Tester", "Web Developer", "Cloud Architect", "Technical Writer", 
                "Network Engineer", "DevOps Engineer", "Data Scientist", "Business Analyst", "IT Consultant", "UX/UI Designer"]

roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=("Arial", 15, "bold"), state="readonly")
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])

# Gender Label
genderLabel = CTkLabel(leftFrame, text="Gender", font=("arial", 18, "bold"), text_color="white")
genderLabel.grid(row=4, column=0, padx=20, pady=10, sticky="w")

gender_options = ["Male", "Female"]

genderBox = CTkComboBox(leftFrame, values=gender_options, width=180, font=("Arial", 15, "bold"), state="readonly")
genderBox.grid(row=4, column=1)
genderBox.set(gender_options[0])

# Salary Label
salaryLabel = CTkLabel(leftFrame, text="Salary", font=("arial", 18, "bold"), text_color="white")
salaryLabel.grid(row=5, column=0, padx=20, pady=10, sticky="w")

salaryEntry = CTkEntry(leftFrame, font=("arial", 15, "bold"), width=180)
salaryEntry.grid(row=5, column=1)

# Right Frame
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Configuring right frame grid to handle resizing
rightFrame.grid_rowconfigure(1, weight=1)
rightFrame.grid_columnconfigure((0, 1, 2, 3), weight=1)

search_options = ["Id", "Name", "Phone", "Role", "Gender", "Salary"]

searchBox = CTkComboBox(rightFrame, values=search_options, state="readonly")
searchBox.grid(row=0, column=0, padx=5, pady=5)
searchBox.set("Search By")

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1, padx=5, pady=5)

# Search Button
searchButton = CTkButton(rightFrame, text="Search", width=100)
searchButton.grid(row=0, column=2, padx=5, pady=5)

# Show All Button
showallButton = CTkButton(rightFrame, text="Show All", width=100)
showallButton.grid(row=0, column=3, padx=5, pady=5)

# Treeview
tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

tree["columns"] = ("Id", "Name", "Phone", "Role", "Gender", "Salary")

tree.heading("Id", text="Id")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Role", text="Role")
tree.heading("Gender", text="Gender")
tree.heading("Salary", text="Salary")

tree.config(show="headings")

tree.column("Id", width=50)
tree.column("Name", width=150)
tree.column("Phone", width=120)
tree.column("Role", width=140)
tree.column("Gender", width=70)
tree.column("Salary", width=100)

# Treeview Style
style = ttk.Style()
style.configure("Treeview.Heading", font=("arial", 14, "bold"))
style.configure("Treeview", font=("arial",13,"bold"),rowheight=50,background="#161c30",foreground="white")

# Scrollbar
scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=4, sticky="ns")

# Button Frame
buttonFrame = CTkFrame(window, fg_color="#161C30")
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

# New Button
newButton = CTkButton(buttonFrame, text="New Employee", font=("arial", 15, "bold"), width=160, corner_radius=15)
newButton.grid(row=0, column=0, pady=5, padx=10)

# Add Button
addButton = CTkButton(buttonFrame, text="Add Employee", font=("arial", 15, "bold"), width=160, corner_radius=15, command=add_employee)
addButton.grid(row=0, column=1, pady=5, padx=10)

# Update Employee Button
updateButton = CTkButton(buttonFrame, text="Update Employee", font=("arial", 15, "bold"), width=160, corner_radius=15, command=update_employee)
updateButton.grid(row=0, column=2, pady=5, padx=10)

# Delete Employee Button
deleteButton = CTkButton(buttonFrame, text="Delete Employee", font=("arial", 15, "bold"), width=160, corner_radius=15, command=delete_employee)
deleteButton.grid(row=0, column=3, pady=5, padx=10)

# Delete All Employee Button
deleteallButton = CTkButton(buttonFrame, text="Delete All", font=("arial", 15, "bold"), width=160, corner_radius=15, command=delete_all_employees)
deleteallButton.grid(row=0, column=4, pady=5, padx=10)

# Adjusting the window grid to ensure proper resizing
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

# Initializing the data in the Treeview


treeview_data()

window.bind("<ButtonRelease>",selection)

window.mainloop()

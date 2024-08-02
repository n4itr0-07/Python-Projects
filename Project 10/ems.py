from customtkinter import *
from PIL import Image
from tkinter import ttk

# Main Window
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

role_options = ["Security Architect", "Penetration Tester", "Web Developer", "Cloud Architect", "Technical Writer", "Network Engineer", "DevOps Engineer", "Data Scientist", "Business Analyst", "IT Consultant", "UX/UI Designer"]

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

# Scrollbar
scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=4, sticky="ns")

# Button Frame
buttonFrame = CTkFrame(window, fg_color="#161C30")
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

# New Button
newButton = CTkButton(buttonFrame, text="New Employee", font=("arial", 15, "bold"), width=160, corner_radius=15)
newButton.grid(row=0, column=0, pady=5)

# Add Button
addButton = CTkButton(buttonFrame, text="Add Employee", font=("arial", 15, "bold"), width=160, corner_radius=15)
addButton.grid(row=0, column=1, pady=5, padx=5)

# Update Employee Button
updateButton = CTkButton(buttonFrame, text="Update Employee", font=("arial", 15, "bold"), width=160, corner_radius=15)
updateButton.grid(row=0, column=2, pady=5, padx=5)

# Delete Employee Button
deleteButton = CTkButton(buttonFrame, text="Delete Employee", font=("arial", 15, "bold"), width=160, corner_radius=15)
deleteButton.grid(row=0, column=3, pady=5, padx=5)

# Delete All Employee Button
deleteallButton = CTkButton(buttonFrame, text="Delete All", font=("arial", 15, "bold"), width=160, corner_radius=15)
deleteallButton.grid(row=0, column=4, pady=5, padx=5)

# Adjusting the window grid to ensure proper resizing
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()

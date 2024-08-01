from customtkinter import *
from PIL import Image
from tkinter import ttk

window = CTk()
window.geometry("930x580")
window.resizable(0,0)
window.title("Employee Management System")
window.configure(fg_color="#161C30")


logo = CTkImage(Image.open("Images/header.jpeg"),size=(900,158))
logoLabel = CTkLabel(window,image=logo,text="")
logoLabel.grid(row=0,column=0,columnspan=2)


leftFrame = CTkFrame(window,fg_color="#161C30")
leftFrame.grid(row=1,column=0)

#ID Label

idLabel = CTkLabel(leftFrame,text="Id",font=("arial",18,"bold"),text_color="white")
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky="w")

idEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
idEntry.grid(row=0,column=1)


# Name Label

nameLabel = CTkLabel(leftFrame,text="Name",font=("arial",18,"bold"),text_color="white")
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky="w")

nameEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
nameEntry.grid(row=1,column=1)

#Phone Label

phoneLabel = CTkLabel(leftFrame,text="Phone",font=("arial",18,"bold"),text_color="white")
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky="w")

phoneEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
phoneEntry.grid(row=2,column=1)

# Role Label

roleLabel = CTkLabel(leftFrame,text="Role",font=("arial",18,"bold"),text_color="white")
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky="w")

role_options = ["Security Architect","Penetrartion Tester","Web Developer","Colud Architect","Technial Writer","Network Engineer","DevOps Engineer","Data Scientist","Business Analyst","IT Consultant","UX/Ui Designer"]

roleBox = CTkComboBox(leftFrame,values=role_options,width=180,font=("Arial",15,"bold"),state="readonly")
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

#Gender label

genderLabel = CTkLabel(leftFrame,text="Gender",font=("arial",18,"bold"),text_color="white")
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky="w")

gender_options = ["Male","Female"]

genderBox = CTkComboBox(leftFrame,values=gender_options,width=180,font=("Arial",15,"bold"),state="readonly")
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0])

#Salary label

salaryLabel = CTkLabel(leftFrame,text="Salary",font=("arial",18,"bold"),text_color="white")
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky="w")

salaryEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
salaryEntry.grid(row=5,column=1)


#TODO: RIGHT FRAME
rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1)


search_options = ["Id", "Name", "Phone", "Role", "Gender", "Salary"]

searchBox = CTkComboBox(rightFrame,values=search_options,state="readonly")
searchBox.grid(row=0,column=0)
searchBox.set("Search By")

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)


#TODO: SEARCH BUTTON 

searchButton = CTkButton(rightFrame,text="Serach",width=100)
searchButton.grid(row=0,column=2)

#TODO: SHOW ALL  BUTTON
showallButton = CTkButton(rightFrame,text="Show All",width=100)
showallButton.grid(row=0,column=3,pady=5)


tree = ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)


tree["columns"] = ("Id", "Name","Phone", "Role", "Gender", "Salary")

tree.heading("Id",text="Id")
tree.heading("Name",text="Name")
tree.heading("Phone",text="Phone")
tree.heading("Role",text="Role")
tree.heading("Gender",text="Gender")
tree.heading("Salary",text="Salary")

tree.config(show="headings")

tree.column("Id",width=80)
tree.column("Name",width=160)
tree.column("Phone",width=160)
tree.column("Role",width=200)
tree.column("Gender",width=100)
tree.column("Salary",width=100)


style = ttk.Style()

style.configure("Treeview.Heading",font=("arial",18,"bold"))




window.mainloop()
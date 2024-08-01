from customtkinter import *
from PIL import Image
from tkinter import messagebox


def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "Please enter both username and password.")

    elif usernameEntry.get() == "Saliko" or passwordEntry.get() == "12345":
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        root.destroy()
        import ems
        
    else:
        messagebox.showerror("Error", "Invalid username or password.")
  


root=CTk()
root.geometry("940x500")
root.resizable(0,0)
root.title("login page")


image = CTkImage(Image.open("images/background.png"),size=(930,500))

imageLabel = CTkLabel(root,image=image,text="")
imageLabel.place(x=0,y=0)

headinglabel = CTkLabel(root,text="Employee Management System",bg_color="#fafafa",font=("Goudy Old Style",20, "bold"),text_color="dark blue")
headinglabel.place(x=350,y=210)


usernameEntry = CTkEntry(root,placeholder_text="Enter Your Username",width=180)
usernameEntry.place(x=400,y=250)

passwordEntry = CTkEntry(root,placeholder_text="Enter Your Password",width=180,show="*")
passwordEntry.place(x=400,y=290)

loginButton = CTkButton(root,text="Login",cursor="hand2",command=login)
loginButton.place(x=419,y=340)




root.mainloop()
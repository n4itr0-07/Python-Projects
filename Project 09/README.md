# Shareit File Transfer Application

This guide will walk you through the creation of a simple file transfer application using Python and Tkinter. The application allows users to send and receive files over a local network.

## Prerequisites

Make sure you have the following installed:
- [Python](https://www.python.org/downloads/)
- Tkinter library (comes with standard Python installations)
- Basic understanding of Python programming

## The Code

```python
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

# Initialize the main window
root = Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

# Define the Send function
def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    # Function to select a file
    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select Image File",
                                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

    # Function to send the selected file
    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print("Waiting for any incoming connections ....")
        conn, addr = s.accept()
        file = open(filename, "rb")
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")

    # Icon and background images
    image_icon1 = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/sender.png")
    Label(window, image=Sbackground).place(x=2, y=0)

    Mbackground = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/id.png")
    Label(window, image=Mbackground, bg="#f4fdfe").place(x=100, y=260)

    # Display host ID
    host = socket.gethostname()
    Label(window, text=f"ID: {host}", bg="white", fg="black").place(x=140, y=290)

    # Buttons for file selection and sending
    Button(window, text="Select File", width=10, height=1, font="arial 14 bold", bg="#fff", fg="#000", command=select_file).place(x=160, y=150)
    Button(window, text="SEND", width=8, height=1, font="arial 14 bold", bg="#000", fg="#fff", command=sender).place(x=300, y=150)

    window.mainloop()

# Define the Receive function
def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    # Function to receive the file
    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        file = open(filename1, "wb")
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")

    # Icon and background images
    image_icon1 = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/receive.png")
    main.iconphoto(False, image_icon1)

    Hbackground = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/receiver.png")
    Label(main, image=Hbackground).place(x=2, y=0)

    logo = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/profile.png")
    Label(main, image=logo, bg="#f4fdfe").place(x=10, y=250)

    Label(main, text="Receive", font=("arial", 20), bg="#f4fdfe").place(x=100, y=280)

    # Input fields for sender ID and incoming file name
    Label(main, text="Input sender id", font=("arial", 10, "bold"), bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry(main, width=25, fg="black", bg="white", font=("arial", 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(main, text="filename for the incoming file", font=("arial", 10, "bold"), bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(main, width=25, fg="black", bg="white", font=("arial", 15))
    incoming_file.place(x=20, y=450)

    imageicon = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/arrow.png")
    rr = Button(main, text="Receive", compound=LEFT, image=imageicon, width=130, bg="#39c790", font="arial 14 bold", command=receiver)
    rr.place(x=20, y=500)

    main.mainloop()

# Main window icon and layout
image_icon = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/icon.png")
root.iconphoto(False, image_icon)

Label(root, text="File Transfer", font=("Acumin Variable Concept", 20, "bold"), bg="#f4fdfe").place(x=20, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

send_image = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/send.png")
send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
send.place(x=50, y=100)

receive_image = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/receive.png")
receive = Button(root, image=receive_image, bg="#f4fdfe", bd=0, command=Receive)
receive.place(x=300, y=100)

Label(root, text="Send", font=("Acumin Variable Concept", 17, "bold"), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=("Acumin Variable Concept", 17, "bold"), bg="#f4fdfe").place(x=300, y=200)

background = PhotoImage(file="C:/Code With Ssn/Learning Python/Python-Projects/Project 9/Image/background.png")
Label(root, image=background).place(x=2, y=323)

root.mainloop()
```

## Detailed Explanation

### 1. Importing Libraries

```python
from tkinter import *  # Import all classes and functions from the tkinter library
import socket  # Import the socket module for network connections
from tkinter import filedialog  # Import filedialog to open file dialog windows
from tkinter import messagebox  # Import messagebox to show dialog boxes
import os  # Import os module to interact with the operating system
```

- `tkinter`: Provides tools to create graphical user interfaces.
- `socket`: Allows communication over a network.
- `filedialog`: Enables file selection dialog boxes.
- `messagebox`: Displays message boxes.
- `os`: Provides functions to interact with the operating system.

### 2. Creating the Main Window

```python
root = Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)
```

- `Tk()`: Initializes the Tkinter application.
- `title()`: Sets the window title.
- `geometry()`: Sets the window size and position.
- `configure()`: Sets the background color.
- `resizable()`: Disables window resizing.

### 3. Defining the Send Function

```python
def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)
```

- `Toplevel()`: Creates a new window on top of the main window.

#### 3.1. File Selection

```python
    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select Image File",
                                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
```

- `askopenfilename()`: Opens a dialog box to select a file.
- `initialdir`: Sets the initial directory for the file dialog.
- `title`: Sets the title of the file dialog.
- `filetypes`: Sets

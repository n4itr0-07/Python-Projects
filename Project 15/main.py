# Import necessary libraries
import tkinter as tk  # Tkinter for GUI
from tkinter import messagebox  # To display message boxes
import re  # Regular expressions to check password patterns

# Function to check the password strength
def check_password_strength(password):
    """
    This function checks the strength of the given password based on criteria:
    - Length of the password
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of numbers
    - Presence of special characters
    """
    
    # Initialize score for password strength
    score = 0
    
    # Criteria 1: Check if the password length is at least 8 characters
    if len(password) >= 8:
        score += 1
    
    # Criteria 2: Check if the password contains both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    
    # Criteria 3: Check if the password contains numbers
    if re.search(r'[0-9]', password):
        score += 1
    
    # Criteria 4: Check if the password contains special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Determine the password strength based on the score
    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

# Function to update the password strength label in the GUI
def update_strength_label():
    """
    This function retrieves the password from the entry widget,
    calls the password strength checking function, and updates the GUI
    with the strength result.
    """
    
    # Get the password from the entry widget
    password = password_entry.get()
    
    # Check the strength of the password using the function
    strength = check_password_strength(password)
    
    # Update the label color and text based on the strength
    if strength == "Strong":
        strength_label.config(text="Password Strength: Strong", fg="green")
    elif strength == "Medium":
        strength_label.config(text="Password Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Password Strength: Weak", fg="red")

# Function to display information about password rules
def show_info():
    """
    This function displays a message box containing information about
    the password strength rules.
    """
    messagebox.showinfo("Password Strength Info", 
                        "Your password should contain:\n"
                        "- At least 8 characters\n"
                        "- Both uppercase and lowercase letters\n"
                        "- At least one number\n"
                        "- At least one special character (!@#$%^&*)")

# Create the main window (root)
root = tk.Tk()  # Initialize the Tkinter root window
root.title("Password Strength Checker")  # Set the window title
root.geometry("400x250")  # Set the window size

# Create and place the password entry field
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=10)  # Add some padding around the label

password_entry = tk.Entry(root, show="*", width=30)  # Password field with masked input
password_entry.pack(pady=5)

# Create and place a button that checks the password strength
check_button = tk.Button(root, text="Check Strength", command=update_strength_label)
check_button.pack(pady=10)

# Create a label to display the password strength result
strength_label = tk.Label(root, text="Password Strength: ", font=("Helvetica", 12))
strength_label.pack(pady=20)

# Create a menu to display password rules
menu = tk.Menu(root)  # Initialize the menu
root.config(menu=menu)  # Set the menu for the root window

# Add 'Help' to the menu and link it to the show_info function
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Password Rules", command=show_info)

# Start the Tkinter main loop
root.mainloop()

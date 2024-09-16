# Password Strength Checker

This is a simple password strength checker application built using Python and Tkinter. The application evaluates the strength of a password based on several criteria and provides feedback to the user.

## Features

- **Password Strength Evaluation**: Checks the password for length, presence of uppercase and lowercase letters, numbers, and special characters.
- **Graphical User Interface (GUI)**: User-friendly interface to enter the password and view the strength.
- **Password Rules Information**: Provides information about the criteria for a strong password.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `re` module (included with Python)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Salik-Seraj/Python-Projects
    cd Project 15
    ```

2. **Run the application**:
    ```sh
    python password_strength_checker.py
    ```

## Usage

1. **Enter your password**: Type your password into the entry field.
2. **Check Strength**: Click the "Check Strength" button to evaluate the password.
3. **View Results**: The strength of the password will be displayed as "Strong", "Medium", or "Weak" with corresponding colors (green, orange, red).
4. **Password Rules**: Click on the "Help" menu and select "Password Rules" to view the criteria for a strong password.

## Code Overview

### Import Libraries

```python
import tkinter as tk
from tkinter import messagebox
import re
```

### Password Strength Checking Function

```python
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"
```

### Update Strength Label Function

```python
def update_strength_label():
    password = password_entry.get()
    strength = check_password_strength(password)
    if strength == "Strong":
        strength_label.config(text="Password Strength: Strong", fg="green")
    elif strength == "Medium":
        strength_label.config(text="Password Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Password Strength: Weak", fg="red")
```

### Show Info Function

```python
def show_info():
    messagebox.showinfo("Password Strength Info", 
                        "Your password should contain:\n"
                        "- At least 8 characters\n"
                        "- Both uppercase and lowercase letters\n"
                        "- At least one number\n"
                        "- At least one special character (!@#$%^&*)")
```

### GUI Setup

```python
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=update_strength_label)
check_button.pack(pady=10)

strength_label = tk.Label(root, text="Password Strength: ", font=("Helvetica", 12))
strength_label.pack(pady=20)

menu = tk.Menu(root)
root.config(menu=menu)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Password Rules", command=show_info)

root.mainloop()
```
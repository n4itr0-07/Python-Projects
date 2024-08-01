# Password Generator Project

## Introduction

This project will guide you through creating a simple password generator using Python. The program will ask the user if they want to generate a password, and if the user agrees, it will generate a random password based on the specified length.

## Prerequisites

Before you start, make sure you have Python installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).

## Step-by-Step Guide

### Step 1: Import Necessary Libraries

First, we need to import the required libraries for our project. We will use the `string` and `random` libraries.

```python
import string
import random
```

### Step 2: Define the Character Set

We need to define a list of characters that our password can include. This includes uppercase and lowercase letters, digits, and some special characters.

```python
characters = list(string.ascii_letters + string.digits + "!@#$%^&*&?/.,()")
```

### Step 3: Create the Password Generator Function

Next, we will define a function `generate_password` that will generate a random password based on the user's specified length.

```python
def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    
    password = "".join(password)
    print(password)
```

### Step 4: Ask User for Input

We will prompt the user to decide if they want to generate a password. Based on their input, we will either generate the password or exit the program.

```python
option = input("Do you want to generate a password (Y/N): ")

if option == "Y":
    generate_password()
elif option == "N":
    print("Okay, no problem. Have a great day!")
else:
    print("Invalid option. Please try again.")
    quit()
```

### Complete Code

Here is the complete code for the password generator project:

```python
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*&?/.,()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    
    password = "".join(password)
    print(password)

option = input("Do you want to generate a password (Y/N): ")

if option == "Y":
    generate_password()
elif option == "N":
    print("Okay, no problem. Have a great day!")
else:
    print("Invalid option. Please try again.")
    quit()
```

## Running the Code

To run the code, save it in a file named `password_generator.py` and execute it using the command:

```bash
python password_generator.py
```

Follow the prompts to generate your password.

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Python String Library](https://docs.python.org/3/library/string.html)
- [Python Random Library](https://docs.python.org/3/library/random.html)



## Follow Me

If you found this guide helpful, follow me for more tutorials and projects on GitHub and other social media platforms!

- [GitHub](https://github.com/Salik-Seraj)
- [X](https://twitter.com/code_with_ssn)
- [LinkedIn](https://linkedin.com/in/salik-seraj-naik)
- [Personal Website](https://linktr.ee/SalikSerajNaik)
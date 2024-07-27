# Site Connectivity Checker

This project is a simple Python script that checks the connectivity of a given URL. It attempts to open the URL and prints whether the connection was successful along with the response code.

## Prerequisites

Before you start, make sure you have Python installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).

## Step-by-Step Guide

### Step 1: Import Necessary Libraries

First, we need to import the required libraries for our project. We will use the `urllib.request` library.

```python
import urllib.request as urllib
```

### Step 2: Define the Main Function

Next, we will define a function `main` that will take a URL as input and check its connectivity.

```python
def main(url):
    print("Checking for Site Connectivity ..")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was :", response.getcode())
```

### Step 3: Prompt User for Input

We will prompt the user to enter the URL of the site they want to check for connectivity.

```python
print("This is a Site Connectivity Checker")
input_url = input("Enter the URL of the site: ")
```

### Step 4: Call the Main Function

Finally, we will call the `main` function with the user-provided URL.

```python
main(input_url)
```

### Complete Code

Here is the complete code for the Site Connectivity Checker project:

```python
import urllib.request as urllib

def main(url):
    print("Checking for Site Connectivity ..")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was :", response.getcode())

print("This is a Site Connectivity Checker")
input_url = input("Enter the URL of the site: ")

main(input_url)
```

## Running the Code

To run the code, save it in a file named `site_connectivity_checker.py` and execute it using the command:

```bash
python site_connectivity_checker.py
```

Follow the prompts to check the connectivity of your desired URL.

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [urllib.request Library](https://docs.python.org/3/library/urllib.request.html)

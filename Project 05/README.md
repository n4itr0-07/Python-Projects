# Typing Speed and Accuracy Calculator

This Python program calculates your typing speed and accuracy by comparing your input against a predefined set of paragraphs. Follow the steps below to use this program.

## Code

```python
from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    len_partest = len(partest)
    len_usertest = len(usertest)
    min_len = min(len_partest, len_usertest)
    
    for i in range(min_len):
        if partest[i] != usertest[i]:
            error += 1
            
    # Count the remaining characters as errors
    error += abs(len_partest - len_usertest)
    return error

def speed_time(time_s, time_e):
    time_delay = time_e - time_s
    minutes = int(time_delay // 60)
    seconds = int(time_delay % 60)
    return minutes, seconds

if __name__ == "__main__":
    paragraphs = [
        "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea. A paragraph consists of one or more sentences. Though not required by the syntax of any language, paragraphs are usually an expected part of formal writing, used to organize longer prose.",
        "My name is Salik Seraj Naik. I am currently learning various programming languages and working on improving my technical skills. I have a passion for cybersecurity and data science, and I am looking forward to contributing to these fields.",
        "Follow me on various social media platforms to stay updated with my latest projects and achievements. I am actively engaged in sharing knowledge and collaborating with others in the tech community.",
        "Python is a powerful programming language that is widely used in various domains such as web development, data science, artificial intelligence, and more. Its simplicity and readability make it a popular choice for beginners and experts alike.",
        "Machine learning is a subset of artificial intelligence that focuses on building systems that learn from data. These systems improve their performance over time without being explicitly programmed. Applications of machine learning can be found in numerous fields, including healthcare, finance, and marketing.",
        "Cybersecurity is a critical aspect of modern technology. With the increasing reliance on digital systems, protecting sensitive information from cyber threats has become more important than ever. Understanding the principles of cybersecurity and implementing best practices can help safeguard data and ensure the integrity of systems."
    ]
    
    r.shuffle(paragraphs)
    index = 0
    total_paragraphs = len(paragraphs)

    while True:
        ck = input("Ready to test: Yes / No: ")
        if ck.lower() == "yes":
            if index >= total_paragraphs:
                print("No more paragraphs left to test. Thank you!")
                break

            test1 = paragraphs[index]
            index += 1

            print("******Typing Speed Calculator*******")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Enter: ")
            time_2 = time()
    
            minutes, seconds = speed_time(time_1, time_2)
            print(f"Time taken: {minutes} minutes and {seconds} seconds")
            print("Errors: ", mistake(test1, testinput))
    
        elif ck.lower() == "no":
            print("Thank you")
            break
        else:
            print("Invalid input! Try again...")
```

## Step-by-Step Guide

1. **Import necessary modules**:
   - `time`: To measure the time taken for typing.
   - `random`: To shuffle the list of paragraphs.

2. **Define the `mistake` function**:
   - This function calculates the number of errors between the given paragraph and the user's input.

3. **Define the `speed_time` function**:
   - This function calculates the time taken for typing in minutes and seconds.

4. **Main Program**:
   - Create a list of paragraphs to test typing speed and accuracy.
   - Shuffle the list of paragraphs to provide a random paragraph each time.
   - Use a while loop to repeatedly ask the user if they are ready for the test.
     - If the user inputs "yes":
       - Check if there are more paragraphs left to test.
       - Display the paragraph and start the timer.
       - Take the user's input and stop the timer.
       - Calculate and display the time taken and the number of errors.
     - If the user inputs "no":
       - Thank the user and exit the loop.
     - If the input is invalid, prompt the user to try again.

## Usage

1. Run the script.
2. Follow the prompts in the terminal/command line.
3. Type the displayed paragraph as accurately and quickly as possible.
4. View your typing speed and accuracy results.
5. Repeat or exit as desired.
---

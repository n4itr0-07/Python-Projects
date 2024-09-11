# 🎉 Number Guessing Game

Welcome to the Number Guessing Game! This is a simple yet fun game where you try to guess a randomly generated number between 1 and 100. The game gives you hints if your guess is too low or too high, and it counts how many attempts you take to guess the correct number.

## Features

- **Random Number Generation**: The game generates a random number between 1 and 100 for you to guess.
- **Input Validation**: Ensures that the input is a valid number within the range.
- **Hints**: Provides feedback on whether your guess is too low or too high.
- **Attempts Counter**: Tracks how many attempts you take to guess the correct number.
- **Custom Messages**: Fun and engaging messages, enhanced with emojis, to keep you motivated.

## How to Play

1. **Run the Game**: Start the game, and you will be greeted with a welcome message.
2. **Make a Guess**: Enter your guess (a number between 1 and 100).
3. **Receive Feedback**: The game will tell you if your guess is too low, too high, or correct.
4. **Keep Guessing**: If your guess is incorrect, keep guessing until you find the correct number.
5. **Win the Game**: Once you guess the correct number, the game will congratulate you and tell you how many attempts you took.

## Code Overview

Below is the code for the Number Guessing Game:

```python
import random

def print_welcome_message():
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number. You'll get hints if your guess is too low or too high.")
    print("Let's see how quickly you can guess it! 🤔")

def print_try_again_message():
    print("🔄 Try again!")

def print_invalid_input_message():
    print("❌ Invalid input. Please enter a number between 1 and 100.")

def print_too_low_message():
    print("⬆️ Too low! Try again!")

def print_too_high_message():
    print("⬇️ Too high! Try again!")

def print_congratulations_message():
    print("🎉 Congratulations! You guessed the correct number! 🎉")

def main():
    print_welcome_message()
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            
            if guess < 1 or guess > 100:
                print_invalid_input_message()
                continue
            
            attempts += 1
            
            if guess < number_to_guess:
                print_too_low_message()
            elif guess > number_to_guess:
                print_too_high_message()
            else:
                print_congratulations_message()
                print(f"It took you {attempts} attempts to guess the number.")
                break
        except ValueError:
            print_invalid_input_message()

if __name__ == "__main__":
    main()
```

## Step-by-Step Guide

### 1. Install Python

Ensure you have Python installed on your machine. If not, download and install Python from the [official website](https://www.python.org/downloads/).

### 2. Clone or Download the Repository

You can clone this repository or download the `number_guessing_game.py` file to your local machine.

### 3. Run the Game

Open a terminal or command prompt, navigate to the directory containing `number_guessing_game.py`, and run the game using the following command:

```bash
python number_guessing_game.py
```

### 4. Play the Game

Follow the on-screen instructions to play the game. Try to guess the number, and the game will guide you with hints and feedback.

### 5. Modify the Game

Feel free to modify the game by adding more features or changing the messages. Explore Python and have fun learning!
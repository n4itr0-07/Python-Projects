# Rock, Paper, Scissors Game

Welcome to the **Rock, Paper, Scissors** game! This simple command-line game allows you to play the classic game against the computer with a fun, emoji-filled interface.

## Features

- Play Rock, Paper, Scissors against the computer.
- Track scores for both the user and the computer.
- Fun visual design using emojis.
- Easy to use and understand.

![rps](https://github.com/user-attachments/assets/f2d46b98-3d8c-4143-a94d-a7e20eb909ba)


## Getting Started

Follow these steps to get the game up and running on your local machine.

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the repository** (if hosted on GitHub) or copy the code directly from below.

2. **Create a new Python file** (e.g., `rock_paper_scissors.py`) and paste the provided code into the file.

### How to Play

1. **Run the game** by executing the Python file in your terminal or command prompt.

    ```bash
    python rock_paper_scissors.py
    ```

2. **Choose your move** when prompted by typing:
   - `r` for Rock
   - `p` for Paper
   - `s` for Scissors

3. The computer will randomly choose its move, and the winner of the round will be determined according to the classic rules of Rock, Paper, Scissors:
   - Rock crushes Scissors.
   - Scissors cut Paper.
   - Paper covers Rock.

4. **View the scores** after each round and decide whether to continue playing or quit.

5. **To exit the game**, type `n` when prompted to play another round.

## Game Code

```python
import random

# Define emojis and choices
emojis = {"r": "🪨 Rock", "p": "📃 Paper", "s": "✂️ Scissors"}
choices = ("r", "p", "s")

# Initialize scores
user_score = 0
computer_score = 0
rounds_played = 0

# Game loop
while True:
    print("\n" + "="*10 + " Let's Play Rock, Paper, Scissors! " + "="*10)
    
    user_choice = input("Choose Rock, Paper, or Scissors (r/p/s): ").lower()
    if user_choice not in choices:
        print("❌ Invalid Choice! Please choose 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(choices)

    # Display choices
    print("\n" + "-"*40)
    print(f"🧍‍♂️ You chose: {emojis[user_choice]}")
    print(f"💻 Computer chose: {emojis[computer_choice]}")
    print("-"*40)

    # Determine the outcome
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")
    ):
        print("🎉 You Win! 🎉")
        user_score += 1
    else:
        print("😢 You Lose!")
        computer_score += 1

    # Show current scores
    rounds_played += 1
    print("\n" + "="*10 + " Current Scores " + "="*10)
    print(f"🧍‍♂️ You: {user_score}  |  💻 Computer: {computer_score}")
    print(f"Rounds Played: {rounds_played}")
    print("="*40)

    # Continue or exit the game
    should_continue = input("\nDo you want to play another round? (y/n): ").lower()
    if should_continue == "n":
        print("👋 Thanks for playing! See you next time!")
        break

# Dice Rolling Game

This is a fun and interactive Python game that simulates rolling two six-sided dice. Players can roll the dice over multiple rounds, and the game keeps track of the total score. If a player rolls doubles, they're notified with a special message. The game ends when the player either reaches 50 points or decides to stop playing.

## How It Works

### Importing the Random Module

```python
import random
```

The `random` module is imported to generate random numbers, which are used to simulate rolling the dice. Each die can land on a number between 1 and 6.

### Function to Roll the Dice

```python
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2
```

- **`roll_dice` function**: This function simulates the roll of two dice.
- **`die1 = random.randint(1, 6)`**: Generates a random integer between 1 and 6 for the first die.
- **`die2 = random.randint(1, 6)`**: Generates a random integer between 1 and 6 for the second die.
- **`return die1, die2`**: Returns the values of the two dice as a tuple.

### Function to Play the Game

```python
def play_game():
    total_score = 0
    roll_history = []
    rounds = 5  # You can adjust the number of rounds
```

- **`total_score = 0`**: Initializes the total score to zero.
- **`roll_history = []`**: Creates an empty list to store the history of rolls.
- **`rounds = 5`**: Sets the number of rounds for the game. This can be adjusted as needed.

### Displaying the Welcome Message

```python
print("🎲 Welcome to the Dice Rolling Game! 🎲")
print("=" * 35)
```

- **`print("🎲 Welcome to the Dice Rolling Game! 🎲")`**: Displays a welcome message to the player.
- **`print("=" * 35)`**: Prints a decorative line to separate the welcome message from the rest of the game.

### Rolling the Dice and Scoring

```python
for round_num in range(1, rounds + 1):
    print(f"\n🔄 Round {round_num} 🔄")
    choice = input("Roll the dice? (y/n): ").lower()
```

- **`for round_num in range(1, rounds + 1):`**: Loops through the specified number of rounds.
- **`print(f"\n🔄 Round {round_num} 🔄")`**: Displays the current round number.
- **`choice = input("Roll the dice? (y/n): ").lower()`**: Asks the player if they want to roll the dice. The input is converted to lowercase to handle any capitalization.

```python
if choice == "y":
    die1, die2 = roll_dice()
    roll_score = die1 + die2
    total_score += roll_score
    roll_history.append((die1, die2, roll_score))
    print(f"🎲 You rolled: ({die1}, {die2})")
    print(f"💰 Round Score: {roll_score}")
    print(f"🏅 Total Score: {total_score}")
```

- **`if choice == "y":`**: Checks if the player wants to roll the dice.
- **`die1, die2 = roll_dice()`**: Calls the `roll_dice` function to get the values of the two dice.
- **`roll_score = die1 + die2`**: Calculates the score for this roll by summing the values of the two dice.
- **`total_score += roll_score`**: Adds the roll score to the total score.
- **`roll_history.append((die1, die2, roll_score))`**: Stores the roll details (values of the dice and the roll score) in the roll history.
- **`print(f"🎲 You rolled: ({die1}, {die2})")`**: Displays the result of the roll.
- **`print(f"💰 Round Score: {roll_score}")`**: Displays the score for this round.
- **`print(f"🏅 Total Score: {total_score}")`**: Displays the total score so far.

### Checking for Doubles and Winning Condition

```python
if die1 == die2:
    print("🎉 You rolled doubles! 🎉")
```

- **`if die1 == die2:`**: Checks if the two dice have the same value, indicating that the player rolled doubles.
- **`print("🎉 You rolled doubles! 🎉")`**: Notifies the player with a celebratory message that they rolled doubles.

```python
if total_score >= 50:
    print("🎊 You've reached 50 points! You win! 🎊")
    break
```

- **`if total_score >= 50:`**: Checks if the total score has reached or exceeded 50 points.
- **`print("🎊 You've reached 50 points! You win! 🎊")`**: Declares the player a winner if they have reached 50 points.
- **`break`**: Exits the loop, ending the game when the player wins.

### Handling Player's Decision Not to Roll

```python
elif choice == "n":
    print("😔 Thank you for playing! 😔")
    break
```

- **`elif choice == "n":`**: Checks if the player has chosen not to roll the dice.
- **`print("😔 Thank you for playing! 😔")`**: Thanks the player for playing with a sad emoticon.
- **`break`**: Exits the loop, ending the game.

### Handling Invalid Input

```python
else:
    print("⚠️ Invalid choice. Please try again. ⚠️")
```

- **`else:`**: Handles any input that is not 'y' or 'n'.
- **`print("⚠️ Invalid choice. Please try again. ⚠️")`**: Informs the player that their input was invalid and prompts them to try again.

### Displaying the Final Score and Roll History

```python
print("\n🏁 Game Over! 🏁")
print(f"🏆 Final Total Score: {total_score}")
print("📜 Roll History:")
for i, roll in enumerate(roll_history, 1):
    print(f"🔸 Roll {i}: ({roll[0]}, {roll[1]}) - Round Score: {roll[2]}")
print("🙌 Thanks for playing! 🙌")
```

- **`print("\n🏁 Game Over! 🏁")`**: Announces that the game is over.
- **`print(f"🏆 Final Total Score: {total_score}")`**: Displays the player's final total score.
- **`print("📜 Roll History:")`**: Displays a heading for the roll history.
- **`for i, roll in enumerate(roll_history, 1):`**: Iterates over each roll in the roll history, also keeping track of the roll number.
- **`print(f"🔸 Roll {i}: ({roll[0]}, {roll[1]}) - Round Score: {roll[2]}")`**: Displays the details of each roll, including the roll number, the dice values, and the score.
- **`print("🙌 Thanks for playing! 🙌")`**: Thanks the player for participating.

### Loop to Replay the Game

```python
while True:
    play_game()
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != "y":
        print("👋 Goodbye! 👋")
        break
```

- **`while True:`**: Creates an infinite loop that keeps the game running until the player decides to stop.
- **`play_game()`**: Calls the `play_game` function to start a new game.
- **`replay = input("Do you want to play again? (y/n): ").lower()`**: Asks the player if they want to play again and converts the input to lowercase.
- **`if replay != "y":`**: Checks if the player does not want to play again.
- **`print("👋 Goodbye! 👋")`**: Says goodbye to the player with a waving emoticon.
- **`break`**: Exits the loop, ending the program.

## Conclusion

This enhanced dice rolling game is a fun way to practice Python programming concepts such as loops, conditional statements, functions, and list manipulation. The game includes special messages and emojis to make it more engaging. Feel free to modify the game by adjusting the number of rounds, adding new features, or enhancing the user interface.

Happy coding!
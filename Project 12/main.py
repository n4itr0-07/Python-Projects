import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def play_game():
    total_score = 0
    roll_history = []
    rounds = 5  # You can adjust the number of rounds

    for _ in range(rounds):
        choice = input("Roll the dice (y/n): ").lower()

        if choice == "y":
            die1, die2 = roll_dice()
            roll_score = die1 + die2
            total_score += roll_score
            roll_history.append((die1, die2, roll_score))
            print(f"Roll: ({die1}, {die2}) | Round Score: {roll_score} | Total Score: {total_score}")
            
            if die1 == die2:
                print("You rolled doubles!")
                
            if total_score >= 50:
                print("You've reached 50 points! You win!")
                break

        elif choice == "n":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")

    print("\nGame Over!")
    print(f"Final Total Score: {total_score}")
    print("Roll History:")
    for roll in roll_history:
        print(f"({roll[0]}, {roll[1]}) - Round Score: {roll[2]}")
    print("Thanks for playing!")

while True:
    play_game()
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != "y":
        print("Goodbye!")
        break

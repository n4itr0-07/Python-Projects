import random

def print_welcome_message():
    print("\n")
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print("=" * 45)
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number. You'll get hints if your guess is too low or too high.")
    print("Let's see how quickly you can guess it! 🤔")
    print("=" * 45)

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




# # Generate a random number
# # Ask the user to make a guess

# import random


#     # Generate a random number between 1 and 100
# number_to_guess = random.randint(1, 100)
# while True:
#     try:
#         guess = int(input("Guess the number between 1 and 100: "))
#         if guess < number_to_guess:
#             print("Too low! Try again.")
#         elif guess > number_to_guess:
#             print("Too high! Try again.")
#         else:
#             print("Congratulations! You guessed the correct number.")
#             break
#     except ValueError:
#         print("Invalid input. Please enter a number.")
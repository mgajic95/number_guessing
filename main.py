import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Set the difficulty level
    difficulty = input("Choose a difficulty level (easy/medium/hard): ").lower()
    
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty level. Please choose either easy, medium, or hard.")
        return

    # Set the range of numbers based on difficulty
    if difficulty == "easy":
        min_number, max_number = 1, 10
    elif difficulty == "medium":
        min_number, max_number = 1, 50
    else:
        min_number, max_number = 1, 100

    # Generate a random number for the player to guess
    secret_number = random.randint(min_number, max_number)

    attempts = 0
    max_attempts = int((max_number - min_number + 1) * 0.8)  # Adjusted based on difficulty
    score = max_attempts  # Higher score is better

    print(f"\nGuess the number between {min_number} and {max_number}.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ")

        # Validate user input
        if not guess.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            print(f"Your score: {score}")
            break
        else:
            print("Wrong guess. Try again.")
            remaining_attempts = max_attempts - attempts
            print(f"Hints: {get_hint(secret_number, guess)}")
            print(f"Attempts left: {remaining_attempts}")

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

def get_hint(secret, guess):
    if secret > guess:
        return "The secret number is higher."
    else:
        return "The secret number is lower."

# Call the function to play the game
number_guessing_game()

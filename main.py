import random

def number_guessing_game():

    difficulty = input("Choose a difficulty level (easy/medium/hard: ".lower())

    if difficulty == "easy":
        min_number, max_number = 1, 10
        
    elif difficulty == "medium":
        min_number, max_number = 1, 50
    else:
        min_number, max_number = 1, 100

    
    secret_number = random.randint(min_number, max_number)

    attempts = 0
    max_attempts = int((max_number - min_number + 1) * 0.8)
    score = max_attempts
    
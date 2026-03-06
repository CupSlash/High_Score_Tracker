import random

def play_number_guessing():
    target = random.randint(1, 100)
    guesses = 0

    print("\n=== Number Guessing Game (1-100) ===")
    print("Try to guess the number. Fewer guesses = higher score!")

    while True:
        raw = input("Enter your guess (1-100): ")

        # Validate input
        if not raw.isdigit():
            print("Please enter a whole number between 1 and 100.")
            continue

        guess = int(raw)
        if guess < 1 or guess > 100:
            print("Stay within 1 to 100.")
            continue

        guesses += 1

        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Correct! The number was {target}.")
            break

    

    score = 100 - guesses
    if score < 0:
        score = 0

    print(f"You took {guesses} guesses. Your score: {score}\n")
    return score
#import random
import random
#function for the number guessing game overall
def play_number_guessing():
    #make the target variab;e
    target = random.randint(1, 100)
    #set guesses to 0
    guesses = 0
    #print out the introduction
    print("\n=== Number Guessing Game (1-100) ===")
    print("Try to guess the number. Fewer guesses = higher score!")
    #mwhile true
    while True:
        raw = input("Enter your guess (1-100): ")

        # Validate input
        if not raw.isdigit():
            print("Please enter a whole number between 1 and 100.")
            continue
        #validate even more
        guess = int(raw)
        if guess < 1 or guess > 100:
            print("Stay within 1 to 100.")
            continue
        #track the guesses
        guesses += 1
        #tell the user hints of hot or cold
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Correct! The number was {target}.")
            break

    
    #make the scoring thing
    score = 100 - guesses
    if score < 0:
        score = 0
    #print out final results for the user
    print(f"You took {guesses} guesses. Your score: {score}\n")
    #return score
    return score

#BH, KH, ZC 2nd high_score_tracker.py
import random
def search():
    return username_exists
def check_overlapping():
    search()
    if username_exists == False:
                
    else:
        print("That username has already been taken. Please try again.")
def strength_checker():
    password_validity = False
    while password_validity == False:
        password = input("Please enter your password to play. Your password must match 3 or more of the following requirements: Contains special character (s), contains number (s), contains lowercase letter (s), contains uppercase letter (s), and contains at least 8 characters.\n")
        total = 0
        if len(password) >= 8:
            total += 1
        for char in password:
            if char.isupper():
                total += 1
        if char.islower():
            total += 1
        if char.isdigit():
            total += 1
        if not char.isalnum():
            total += 1
        if password == "password":
            print("Ain't no way your password is password.\n")
            password_validity == False
        if total <= 2:
            print("Password strength: Weak.\n")
            password_validity == False
        elif total == 3:
            print("Password strength: Moderate.\n")
            password_validity == True
        elif total == 4:
            print("Password strength: Strong.\n")
            password_validity == True
        elif total == 5:
            print("Password strength: Secure.\n")
            password_validity == True
        print("Your password strength is a  {total} out of 5.\n")
def sign_in():
         print("Please sign in below\n")
         username = input("What is your username?\n")
         check_overlapping()
         password = input("What is your password?\n")
         strength_checker()
         print("Your username and password have been saved, enjoy the game!\n")
def sign_up():
def logout():
        login_dif_account = input("Would you like to exit (e), or login with a different account (l)?\n")
        if login_dif_account == "e":
                print("Hope to see you again!")
                return
        if login_dif_account == "l":
                sign_in()
def game():
        token_choice = input("Time for a game of Tic-Tac-Toe! Would you like to be X or O?").lower()
        if token_choice == "x":
                token = "X"
        if token_choice == "o":
                token = "O"
        Game_data = {
        }
        starts_game = random.randint (0, 1)
        if starts_game == 0:
        else:
def menu():
    print("Welcome to the High Score Tracker!\n")
    choice = input(" Would you like to play a game of tic-tac-toe? y/n\n")
    while True:
        if choice == "y":
                game()
                choice = input("Would you like to play another? y/n\n") 
        if choice == "n":
                logout()
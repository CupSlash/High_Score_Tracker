#BH, KH, ZC 2nd high_score_tracker.py
import random
import csv
database = "src, High Score Tracker\database.csv"
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
        print("Your password strength is a {total} out of 5.\n")
def admin():
		print("Welcome admin")
		if change:
			number = input("Please enter a number.")
			print(specific information about that user)
			choice = print("Would you like to change \n1. Username, \n2. Password, or \n3. Score?\n")
		if remove:
			choice = input("which user account would you like to remove?")
			Remove all account information from that account.
			Reset numbers
		if add:
			print("Please enter a username, password, and score.")
			Insert account into CSV file
		if quit:
			sign_in()
def search(username):
    search_username = username
    matches = []
    for user in database:
        if search_username in database:
            matches.append(user)
    if len(matches) == 0:
        print("No matching found")
        return False
    else:
        return True
username_exists = True
def check_overlapping(username):
    while True:
        search()
        if username_exists == False:
            print("That username has already been taken. Please try again.")
def sign_in():
    print("Please sign in below\n")
    username = input("What is your username?\n")
    check_overlapping()
    password = input("What is your password?\n")
    strength_checker()
    print("Your username and password have been saved, enjoy the game!\n")
def sign_up():
        print("Please sign in below.\n")
        username = input("What is your username?\n")
        check_overlapping()
        password = input("What is your password?\n")
        strength_checker()
        print("Your username and password have been saved, enjoy the game!\n")
def user_intro():
    choice = None
    while choice != "e" or "n":
        choice = input("Do you want to sign in with an existing account (e), or a brand new account (n)?")
        if choice == "e":
            sign_in()
        elif choice == "n":
            sign_up()
        else:
            print("That is not an option")
def logout():
        login_dif_account = input("Would you like to exit (e), or login with a different account (l)?\n")
        if login_dif_account == "e":
                print("Hope to see you again!")
                return
        if login_dif_account == "l":
                sign_in()
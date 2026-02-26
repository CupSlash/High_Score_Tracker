#BH, KH, ZC 2nd high_score_tracker.py
import json
import os
import hashlib

database = "src, High Score Tracker\database.csv"
users_file = 'users.json'
validity = True
score = 0

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

def load_users():
    if not os.path.exists(users_file):
        return {}
    with open(users_file, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(users_file, 'w') as f:
        json.dump(users, f, indent = 2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up(username, password):
    if username == "":
        return False, "Username cannot be empty, please be smart"
    if ";" in username or "," in username or " " in username:
        return False, "Username cannot have spaces, ;, or ,"
    users = load_users()
    if username in users:
        return False, "Username already exists"
    hashed = hash_password(password)
    users[username] = {"password": hashed}
    save_users(users)
    return True, "User created succesfully, yay"

def sign_in():
    print("Please sign in below\n")
    username = input("What is your username?\n")
    if username in database:
        password = input("What is your password?\n")
        if password in database:
            print("Your username and password have been saved, enjoy the game!\n")
        else:
            print("That password is not in our database, please try again later.")
    else:
        print("That username is not in our database, please try again later.")

def user_intro():
    while True:
        choice = input("Do you want to: \n1.sign up \n2.sign in?: ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        else:
            print("Invalid, please try again.")

def logout():
        login_dif_account = input("Would you like to exit (e), or login with a different account (l)?\n")
        if login_dif_account == "e":
                print("Hope to see you again!")
                return
        if login_dif_account == "l":
                sign_in()
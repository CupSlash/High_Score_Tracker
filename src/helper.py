#BH, KH, ZC 2nd high_score_tracker.py
import json
import os
import hashlib

database = "src/database.csv"
users_file = 'users.json'
validity = True
score = 0
current_user = None

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
                continue
            if total <= 2:
                print("Password strength: Weak.\n")
            elif total in [3, 4]:
                print("Password strength: Moderate.\n")
            elif total == 5:
                print("Password strength: Secure.\n")
        
        print(f"Your password strength is a {total} out of 5.\n")
        password_validity = True
        return password

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

def sign_up():
    users = load_users()
    
    print("Creat a new account!")
    
    while True:
        username = input("Enter a new username: ")

        if username == "":
            print("Username cannot be empty, please be smart")
            continue

        if ";" in username or "," in username or " " in username:
            print("Username cannot have spaces, ;, or ,")
            continue

        if username in users:
            print("Username already exists try to add a number to the end of the username or something")
            continue
        break
        
    password = input("Enter a password: ")
    hashed = hash_password(password)

    users[username] = {
        "password": hashed,
        "score": 0
    }
    save_users(users)
    print("User created succesfully, yay")

def sign_in():
    global current_user
    users = load_users()

    print("Please sign in below\n")
    username = input("What is your username?\n")
    
    if username not in users:
        print("Sorry man, but that username is not in our database\n")
        return False

    password = input("What is your password? ")
    hashed = hash_password(password)

    if users[username]["password"] ==  hashed:
        current_user = username
        print("Your username and password have been saved, enjoy the game!\n")
        return True
    else:
        print("Incorrect password")
        return False

def user_intro():#test
    while True:
        choice = input("Do you want to: \n1.sign up \n2.sign in?: ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        else:
            print("Invalid, please try again.")

def logout():
        global current_user
        choice = input("Would you like to exit (e), or login with a different account (l)?\n")
        if choice == "e":
                current_user = None
                print("lets hope you come back. See ya")
                return
        if choice == "l":
                current_user = None
                sign_in()
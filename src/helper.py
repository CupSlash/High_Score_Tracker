#KH, BH, ZC 2nd high_score_tracker.py
import json
import os
import hashlib


database = "src/database.csv"
users_file = 'users.json'
validity = True
current_user = None
def add_tic_tac_toe_win(current_user):
    
    
    if current_user is None:
        print("You must be logged in to record a win\n")
        return False
    
    users = load_users()
    if current_user not in users:
        print("Current user not found in our database")
        return False
    
    users[current_user]["tic_tac_toe_wins"] = users[current_user].get("tic_tac_toe_wins", 0) + 1
    save_users(users)
    return True
def strength_checker(current_user):
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
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Our database failed to load, resetting now.")
            return {}

def save_users(users):
    with open(users_file, 'w') as f:
        json.dump(users, f, indent = 2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up(current_user):
    users = load_users()
    
    print("Create a new account!")
    
    while True:
        username = input("Enter a new username: ")

        if username.strip() == "":
            print("Username cannot be empty.")
            continue

        if ";" in username or "," in username or " " in username:
            print("Username cannot have spaces, ;, or ,.")
            continue

        if username in users:
            print("Username already exists, please use a different name. (tip: add a number or special character!)")
            continue
        break
        
    password = input("Enter a password: ")
    if password.strip() == "":
        print("Password cannot be empty. \n")
        return False
    
    hashed = hash_password(password)

    users[username] = {
    "password": hashed,
    "score": 0,
    "tic_tac_toe_wins": 0
}
    save_users(users)
    print("User created succesfully! Log in to play!")

def sign_in():
    global current_user
    users = load_users()

    print("Please sign in below.\n")
    username = input("What is your username?\n")
    
    if username not in users:
        print("Could not find that username in our database. Maybe there was a typo?\n")
        return False

    password = input("What is your password?\n")
    hashed = hash_password(password)

    if users[username]["password"] ==  hashed:
        current_user = username
        print("Your username and password have been saved, enjoy the game!\n")
        return current_user
    else:
        print("Incorrect password.")
        return False

def logout(current_user):
        
        choice = input("Would you like to exit (e), or login with a different account (l)?\n")
        if choice == "e":
                current_user = None
                print("Smell you later!")
                return
        if choice == "l":
                current_user = None
                sign_in()
import csv

high_scores_file = "high_scores.csv"

def record_score(final_score, current_user):
    

    if current_user is None:
        print("You must be logged in to record a score.\n")
        return False

    users = load_users()
    if current_user not in users:
        print("Current user not found in the database.")
        return False
    try:
        try:
            final_score_int = int(final_score)
        except ValueError:
            print("Score must be a number.")
            return False
        #keep the best score
        existing = users[current_user].get("score", 0)
        if final_score_int > existing:
            users[current_user]["score"] = final_score_int
            save_users(users)

        file_exists = os.path.exists(high_scores_file)
        with open(high_scores_file, "a", newline="") as f:
                writer = csv.writer(f, delimiter= ";")
                if not file_exists:
                    writer.writerow(["username", "score"])
                writer.writerow([current_user, final_score_int])

        print(f"Score recored for {current_user}: {final_score_int}")
        return True
            
    except Exception as e:
        print(f"Could not record score: {e}")
        return False
def view_high_scores(current_user):
    #gets high scores from file and prints them in order from highest to lowest
    users = load_users()
    scores = []
    with open(high_scores_file, "r") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)  # Skip header
        for row in reader:
            username, score = row
            wins = users.get(username, {}).get("tic_tac_toe_wins", 0)
            scores.append((username, int(score), wins))
    scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    print("=== High Scores ===")
    for username, score, wins in scores:
        print(f"{username}: {score} points, {wins} tic tac toe wins!")
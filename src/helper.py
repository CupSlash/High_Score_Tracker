import json
import os
import hashlib
import csv

database = "src/database.csv"
users_file = "users.json"
high_scores_file = "high_scores.csv"
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


def strength_checker():
    password_validity = False
    while password_validity is False:
        password = input(
            "Please enter your password to play. Your password must match 3 or more "
            "of the following requirements: Contains special character(s), contains "
            "number(s), contains lowercase letter(s), contains uppercase letter(s), "
            "and contains at least 8 characters.\n"
        )
        total = 0
        if password == "password":
            print("Ain't no way your password is password.\n")
            continue
        if len(password) >= 8:
            total += 1
        if any(char.isupper() for char in password):
            total += 1
        if any(char.islower() for char in password):
            total += 1
        if any(char.isdigit() for char in password):
            total += 1
        if any(not char.isalnum() for char in password):
            total += 1
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
    with open(users_file, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Our database failed to load, resetting now.")
            return {}


def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f, indent=2)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def sign_up():
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
        print("Password cannot be empty.\n")
        return False
    hashed = hash_password(password)
    users[username] = {
        "password": hashed,
        "score": 0,
        "tic_tac_toe_wins": 0
    }
    save_users(users)
    print("User created successfully! Log in to play!")
    return True


def sign_in():
    users = load_users()
    print("Please sign in below.\n")
    username = input("What is your username?\n")
    
    if username not in users:
        print("Could not find that username in our database. Maybe there was a typo?\n")
        return None
    password = input("What is your password?\n")
    hashed = hash_password(password)
    if users[username]["password"] == hashed:
        print("Your username and password have been saved, enjoy the game!\n")
        return username
    else:
        print("Incorrect password.")
        return None


def logout(current_user):
    choice = input("Would you like to exit (e), or login with a different account (l)?\n")
    if choice == "e":
        print("Smell you later!")
        return None
    if choice == "l":
        return sign_in()
    return current_user


def record_score(final_score, current_user):
    if current_user is None:
        print("You must be logged in to record a score.\n")
        return False
    users = load_users()
    if current_user not in users:
        print("Current user not found in the database.")
        return False
    try:
        final_score_int = int(final_score)
    except ValueError:
        print("Score must be a number.")
        return False
    try:
        existing = users[current_user].get("score", 0)
        if final_score_int > existing:
            users[current_user]["score"] = final_score_int
            save_users(users)
        file_exists = os.path.exists(high_scores_file)
        with open(high_scores_file, "a", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            if not file_exists:
                writer.writerow(["username", "score"])
            writer.writerow([current_user, final_score_int])
        print(f"Score recorded for {current_user}: {final_score_int}")
        return True
    except Exception as e:
        print(f"Could not record score: {e}")
        return False


def view_high_scores():
    users = load_users()
    scores = []
    if not os.path.exists(high_scores_file):
        print("No high scores yet.")
        return
    with open(high_scores_file, "r") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)
        for row in reader:
            username, score = row
            wins = users.get(username, {}).get("tic_tac_toe_wins", 0)
            scores.append((username, int(score), wins))
    scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    print("=== High Scores ===")
    for username, score, wins in scores:
        print(f"{username}: {score} points, {wins} tic tac toe wins!")
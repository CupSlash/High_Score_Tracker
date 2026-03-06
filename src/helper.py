#KH, BH, ZC 2nd high_score_tracker.py
import json
import os
import hashlib

database = "src/database.csv"
users_file = 'users.json'
validity = True
def add_tic_tac_toe_win(current_user):
    
    if current_user is None:
        print("You must be logged in to record a win\n")
        return False
    
    users = load_users()
    if current_user not in users:
        print("Current user not found in users.json")
        return False
    
    users[current_user]["tic_tac_toe_wins"] += 1
    save_users(users)
    return True

def password_tester(password):
    score = 0
    
    if len(password) >= 8:
        print("Length (8+ characters): Yes") # print yes or no 
        score += 1 # add point if yes
    else:
        print("Length (8+ characters): No") # print yes or no
    upper = False
    for letter in password:
        if letter >= 'A' and letter <= 'Z':
            upper = True
    if upper:
        print("Contains uppercase: Yes") # print yes or no 
        score += 1
    else:
        print("Contains uppercase: No")
    lower = False
    for letter in password:
        if letter >= 'a' and letter <= 'z':
            lower = True
    if lower:
        print("Contains lowercase: Yes")
        score += 1
    else:
        print("Contains lowercase: No")
    has_number = False
    for letter in password:
        if letter >= '0' and letter <= '9':
            has_number = True
    if has_number:
        print("Contains numbers: Yes")
        score += 1
    else:
        print("Contains numbers: No")
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = False
    for letter in password:
        if letter in special:
            has_special = True
    if has_special:
        print("Contains special characters: Yes")
        score += 1
    else:
        print("Contains special characters: No")
    
    print("Strength score:", score, "/ 5")
    
    if score <= 2:
        print("Password strength: Weak")
    elif score == 3:
        print("Password strength: Moderate")
    elif score == 4:
        print("Password strength: Strong")
    elif score == 5:
        print("Password strength: Very Strong")

    return score

def load_users():
    if not os.path.exists(users_file):
        return {}
    with open(users_file, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("user.json is wierd.... resetting to empty")
            return {}

def save_users(users):
    with open(users_file, 'w') as f:
        json.dump(users, f, indent = 2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up():
    users = load_users()
    
    print("Create a new account!")
    
    while True:
        username = input("Enter a new username: ")

        if username == "":
            print("Username cannot be empty, please be smart")
            continue
        
        if username.strip() == "":
            print("Username cannot be empty")
            continue
        if ";" in username or "," in username or " " in username:
            print("Username cannot have spaces, ;, or ,")
            continue

        if username in users:
            print("Username already exists try to add a number to the end of the username or something")
            continue
        break
        
    while True:
        password = input("Enter a password: ")

        if password.strip() == "":
            print("Password cannot be empty. \n")
            continue
    
        score = password_tester(password)

        if score < 3:
            print("Password is too weak, please try again")
            continue
        else:
            break
    
    hashed = hash_password(password)

    users[username] = {
    "password": hashed,
    "score": 0,
    "tic_tac_toe_wins": 0
}
    save_users(users)
    print("User created succesfully, yay")
    

def sign_in():
    users = load_users()

    print("Please sign in below\n")
    username = input("What is your username?\n")
    
    if username not in users:
        print("Sorry man, but that username is not in our database\n")
        return None
    
    password = input("What is your password? ")
    hashed = hash_password(password)

    if users[username]["password"] ==  hashed:
        print("Your username and password have been saved, enjoy the game!\n")
        return username
    else:
        print("Incorrect password")
        return None
def logout():
        
        choice = input("Would you like to exit (e), or login with a different account (l)?\n")
        if choice == "e":
                print("lets hope you come back. See ya")
                return None
        if choice == "l":
                return sign_in()

#record the score stuff
#Kensei Higashi
import csv

high_scores_file = "high_scores.csv"

def record_score(final_score, current_user):
    

    if current_user is None:
        print("You must be logged in to record a score\n")
        return False

    users = load_users()
    if current_user not in users:
        print("Current user not found in users.json")
        return False
    try:
        try:
            final_score_int = int(final_score)
        except ValueError:
            print("Score must be a number")
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
        print(f"COuld not record score: {e}")
        return False

def view_high_scores():

    users = load_users()
    scores = []

    for user, data in users.items():
        scores.append((user, data.get("score", 0), data.get("tic_tac_toe_wins", 0)))
        scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    print("\n=== High Scores ===")
    for username, score, wins in scores:
        print(f"{username}: {score} points, {wins} tc tac toe wins")
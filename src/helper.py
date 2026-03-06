#import needed library
import json
import os
import hashlib
import csv
#define files
database = "src/database.csv"
users_file = "users.json"
high_scores_file = "high_scores.csv"
#make a function for adding the tic tac toe wins
def add_tic_tac_toe_win(current_user):
    #if there is no current player, idiot proof that
    if current_user is None:
        print("You must be logged in to record a win\n")
        return False
    
    users = load_users()
    #if the "current user" is not in the database, freak out on them
    if current_user not in users:
        print("Current user not found in our database")
        return False

    #save tic tac toe wins
    users[current_user]["tic_tac_toe_wins"] = users[current_user].get("tic_tac_toe_wins", 0) + 1
    save_users(users)
    return True

#make a password strength tester
def password_tester(password):
    #set the score to zero
    score = 0

    #if it is bigger than 8 words, say it is good.
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
    #do for the lowercase
    lower = False
    for letter in password:
        if letter >= 'a' and letter <= 'z':
            lower = True
    if lower:
        print("Contains lowercase: Yes")
        score += 1
    else:
        print("Contains lowercase: No")
    #do it for has number
    has_number = False
    for letter in password:
        if letter >= '0' and letter <= '9':
            has_number = True
    if has_number:
        print("Contains numbers: Yes")
        score += 1
    else:
        print("Contains numbers: No")
    #make a var for special
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = False
    for letter in password:
        if letter in special:
            has_special = True
    #check for special variables
    if has_special:
        print("Contains special characters: Yes")
        score += 1
    else:
        print("Contains special characters: No")
    #print out the results of the password strength tester
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

# Make a function for loading users
def load_users():
    if not os.path.exists(users_file):
        return {}
    with open(users_file, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Our database failed to load, resetting now.")
            return {}
#make a function for saving users
def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f, indent=2)

#make a function for hashing the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
#make the function for signing up
def sign_up():
    #make a var where you call the load user
    users = load_users()
    print("Create a new account!")
    #while true loop
    while True:
        username = input("Enter a new username: ")
        if username.strip() == "":
            print("Username cannot be empty.")
            continue
        #idiot proof
        if ";" in username or "," in username or " " in username:
            print("Username cannot have spaces, ;, or ,.")
            continue
        if username in users:
            print("Username already exists, please use a different name. (tip: add a number or special character!)")
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
    print("User created succesfully! Log in to play!")
def sign_in():
    users = load_users()
    print("Please sign in below.\n")
    username = input("What is your username?\n")
    
    if username not in users:
        print("Could not find that username in our database. Maybe there was a typo?\n")
        return None

    password = input("What is your password?\n")
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
                print("Smell ya later!")
                return None
        if choice == "l":
                return sign_in()
#record the score stuff
#Kensei Higashi
import csv
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

#function for viewing high score
def view_high_scores():
    #user is the load user function result
    users = load_users()
    #make an empty list for scores
    scores = []
    #only print top ten high scores, sorted by score and tic tac toe wins as tiebreakers.
    for user, data in users.items():
        scores.append((user, data.get("score", 0), data.get("tic_tac_toe_wins", 0)))
        scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    #and print out the high scores
    print("\n=== High Scores ===")
    for i, (username, score, wins) in enumerate(scores[:10], start=1):
        print(f"{i}. {username}: {score} points, {wins} tic tac toe wins!")

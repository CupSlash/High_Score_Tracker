import json
import os
import hashlib

users_file = 'users.json'#json file, simple

#Load users from json
def load_users():
    if not os.path.exists(users_file):
        return {}
    with open(users_file, 'r') as f:
        return json.load(f)

#save user to json
def save_users(users):
    with open(users_file, 'w') as f:
        json.dump(users, f, indent = 2)

#hash password with sha 256 for security from non-existent hackers. YAyyyyyy
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up(username, password):
    if username == "":
        return False, "Username cannot be empty, please be smart"
    if ";" in username or "," in username or " " in username:
        return False, "Username cannot have spaces, ;, or ,"

    users = load_users()

    #check for duplicates
    if username in users:
        return False, "Username already exists"
    
    #hash the password
    hashed = hash_password(password)

    #save user
    users[username] = {
        "password": hashed
    }
    save_users(users)
    return True, "User created succesfully, yay"

def login(username, password):
    users = load_users()


def main():
    while True:
        choice = input("Do you wanto sign u[ or login? (1 for sign up and 2 for login): ")
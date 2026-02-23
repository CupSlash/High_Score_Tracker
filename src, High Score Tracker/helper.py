#BH, KH, ZC 2nd high_score_tracker.py
database = pass
import random
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
		#Display a numbered list with usernames and passwords
		
		#Change, remove, add scores, or quit
		if change:
			number = input("Please enter a number.")
			Display specific information about that user
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
def search():
    action = input"What would you like to search by\n 1. Numeral\n2. Username\n 3. Password\n 4. Highscore\n 5. Exit\n")
    if action == "1":
        search = input("What is the Numeral of the user you want to search: ").strip().lower()
    elif action == "2":
        search = input("What is the User's name: ").strip().lower()
    elif action == "3":
        pass
    elif action == "4":
        pass
    elif action == "5":
        pass
    else:
        print("Invalid.")
        return
    matches = []
    for user in database:
        if search in database[option].lower():
            matches.append(user)
    #if any of the matching is 0, tell them there is no book in existence
    if len(matches) == 0:
        print("No matching found")
        return 
    #if no probelm, show them their searched book
    for book in matches:
        print(book["title"] + " by " + book["author"])

username_exists = True
def search(): 
    #Ken's search function here
    return username_exists
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
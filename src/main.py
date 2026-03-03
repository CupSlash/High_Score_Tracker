#BH, KH, ZC 2nd High Score Tracker
from helper import *
from game import *
def user_intro():#test
    global current_user
    while True:
        print("Do you want to: \n1.sign up \n2.sign in\n3. Play game\n4. Logout\n5. Exit ")

        choice = input("Choose an options(1-5): ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            if current_user is None:
                print("You must be logged in to play. \n")
            else:
                print(f"Starting game for {current_user}...")
        elif choice == "4":
            if current_user is None:
                print("You're not even logged into log out")
            else:
                logout()
        elif choice == "5":
            print("Smell you later. hehehehhe")               
        else:
            print("Invalid, please try again.")
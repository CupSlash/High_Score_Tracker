#BH, KH, ZC 2nd High Score Tracker
import helper as auth
from test_game import play_number_guessing
from game import game
#from game import *
def user_intro():
    while True:
        print("Do you want to: \n1.sign up \n2.sign in\n3. Play game\n4. Logout\n5. Exit ")

        choice = input("Choose an options(1-5): ")

        if choice == "1":
            auth.sign_up()
        elif choice == "2":
            auth.sign_in()

        elif choice == "3":
            if auth.current_user is None:
                print("You must be logged in to play. \n")
            else:
                print(f"Starting game for {auth.current_user}...")
                final_score = game()
                auth.record_score(final_score)

        elif choice == "4":
            if auth.current_user is None:
                print("You're not even logged into log out")
            else:
                auth.logout()
        elif choice == "5":
            print("Smell you later. hehehehhe")               
        else:
            print("Invalid, please try again.")

user_intro()
#BH, KH, ZC 2nd High Score Tracker
import helper as auth
from game import game
from test_game import play_number_guessing
def user_intro():
    while True:
        print("Do you want to: \n1. Sign up \n2. Sign in\n3. Play number guessing game\n4. Play tic tac toe\n5. view high scores \n6. Logout\n7. Exit ")

        choice = input("Choose an options(1-6): ")

        if choice == "1":
            auth.sign_up()
        elif choice == "2":
            auth.sign_in()

        elif choice == "3":
            if auth.current_user is None:
                print("You must be logged in to play. \n")
            else:
                print(f"Starting game for {auth.current_user}...")
                final_score = play_number_guessing()
                auth.record_score(final_score)

        elif choice == "6":
            if auth.current_user is None:
                print("You're not even logged into log out")
            else:
                auth.logout()
        elif choice == "4":
            print (f"starting game for {auth.current_user}...")
            if game():
                auth.add_tic_tac_toe_win()
        elif choice == "5":
            auth.view_high_scores()
        elif choice == "7":
            print("Smell you later. hehehehhe") 
            break              
        else:
            print("Invalid, please try again.")
user_intro()
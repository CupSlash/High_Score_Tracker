#BH, KH, ZC 2nd High Score Tracker
#test
import helper as auth
from game import game
from test_game import play_number_guessing
def user_intro():
    current_user = None
    while True:
        print("Do you want to: \n1. Sign up \n2. Sign in\n3. Play number guessing game\n4. Play tic tac toe\n5. View high scores \n6. Log out\n7. Exit \n")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            auth.sign_up(user)
        elif choice == "2":
            current_user = auth.sign_in()

        elif choice == "3":
            if current_user is None:
                print("You must be logged in to play. \n")
            else:
                print(f"Starting game for {current_user}...")
                final_score = play_number_guessing()
                auth.record_score(final_score, current_user)

        elif choice == "6":
            if current_user is None:
                print("You're not even logged into log out")
            else:
                current_user = auth.logout()
        elif choice == "4":
            print (f"starting game for {current_user}...")
            if game():
                auth.add_tic_tac_toe_win(current_user)
        elif choice == "5":
            auth.view_high_scores(user)
        elif choice == "7":
            print("Smell you later!") 
            break              
        else:
            print("Invalid, please try again.")

user_intro()
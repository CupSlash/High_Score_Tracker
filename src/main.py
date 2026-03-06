import helper as auth
from game import game
from test_game import play_number_guessing
def user_intro():
    user = None
    while True:
        print("Do you want to: \n1. Sign up \n2. Sign in\n3. Play number guessing game\n4. Play tic tac toe\n5. View high scores \n6. Log out\n7. Exit \n")
        choice = input("Choose an option (1-7): ")
        if choice == "1":
            auth.sign_up()
        elif choice == "2":
            user = auth.sign_in()
        elif choice == "3":
            if user is None:
                print("You must be logged in to play.\n")
            else:
                print(f"Starting game for {user}...")
                final_score = play_number_guessing()
                auth.record_score(final_score, user)
        elif choice == "4":
            if user is None:
                print("You must be logged in to play.\n")
            else:
                print(f"Starting game for {user}...")
                if game():
                    auth.add_tic_tac_toe_win(user)
        elif choice == "5":
            auth.view_high_scores()
        elif choice == "6":
            if user is None:
                print("You are already logged out")
            else:
                user = auth.logout(user)
        elif choice == "7":
            print("Smell you later!")
            break
        else:
            print("Invalid, please try again.")
user_intro()
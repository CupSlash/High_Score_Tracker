#BH, KH, ZC 2nd High Score Tracker
from src.helper import *
from src.game import *
def menu():
    user_intro()
    print("Welcome to the High Score Tracker!\n")
    choice = input(" Would you like to play a game of tic-tac-toe? y/n\n")
    while True:
        if choice == "y":
                game()
                choice = input("Would you like to play another? y/n\n") 
        if choice == "n":
                logout()
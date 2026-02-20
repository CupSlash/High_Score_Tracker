#ZC, BH, KH 2nd game.py
from helper import sign_in
import random
print("Welcome to Tic-Tac-Toe!")
token = input("Would you like to be X, or O?")
board = [1,2,3,4,5,6,7,8,9]
token = [0,0,0,0,0,0,0,0,0]
game_data = { "scores" : {"win_1" : [board[0],board[1],board[2]], "win_2" : [board[3],board[4],board[5]], "win_3" : [board[6],board[7],board[8]], "win_4" : [board[0],board[3],board[6]], "win_5" : [board[1],board[4],board[7]], "win_6" : [board[2],board[5],board[8]], "win_7" : [board[0],board[4],board[8]], "win_8" : [board[2],board[4],board[6]]} }
for item in token:
	for i in item:
		print(item)
start = random.randint(1,2)
if start == 1:
	pass
    #X starts the game
else:
	pass
    #O starts
# confusing --> Increase index of board for user selection
def win_check(token, game_data):
    for win in game_data:
	    pos = 0
	for check in win:
		if check == token:
	        pos += 1
	if pos == 3:
		print("user wins!")
		return True
	else:
		continue
	
#Grid will be displayed as shown
#0 0 0
#0 0 0
#0 0 0
def player_turn():
	pass
#	Print the selection list as shown above
#	While True:
#		The user selects a square. 
#		If that spot is valid
#continue
#Else:
#break
    #win_check(user_token)
def computer_turn():
    computer_luck = random.randint(1,3)
    computer_choice_of_cube = random.randint(1,2)
    choice_of_cube = 0
    if computer_choice_of_cube == 1:
        choice_of_cube = 1
    else:
        choice_of_cube = -1
    for every_item in score_list():
        if computer_luck = 2 or 3
            if item has 
                find index of the item in the list
                indexvar = index of item
                if index of item in display_list does not equal x or O
                    index = index + choice_of_cube
                    Find choice_of_cube in the score list and increase the score of all rows associated with it by 1
                    break out of the for loop
                else:
                continue to next iteration
            else:
                continue to next iteration
                reset computer luck
        else:
        choose random square and do a cell score increase
        break out of the loop
    win_check(computer_token)

def admin():
	print("Welcome admin")
	#Display a numbered list with usernames and passwords
	
	#Change, remove, add scores, or quit
	if change:
		number = input("Please enter a number.")
		Display specific information about that user
		Ask the admin if they want to change 1. Username, 2. Password, or 3. Score
	if remove:
		Ask the admin which user account to remove
		Remove all account information from that account.
		Reset numbers
	if add:
		Admin is prompted to enter a username, password, and score
		Insert account into CSV file
	if quit:
		sign_in()

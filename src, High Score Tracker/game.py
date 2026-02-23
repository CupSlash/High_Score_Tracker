#BH, KH, ZC 2nd game.py
import random
def game():
	global user_token, computer_token, game_data, board, token
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
		user_token = "X"
		computer_token = "Y"
	else:
		user_token = "Y"
		computer_token = "X"
	def win_check(token):
		for win in game_data:
			pos = 0
		for check in win:
			if check == token:
				pos += 1
		if pos == 3:
			return True
		else:
			return False
		

	def player_turn():
		pass
		for x in [token[0], token[1], token[2]]:
			print (x)
		for x in [token[3], token[4], token[5]]:
			print (x)
		for x in [token[6], token[7], token[8]]:
			print (x)
		choice = int(input("please select the index of the square you choose"))
		if token.index(choice) not in ["X", "Y"]:
			token.index(choice) = user_token
		if win_check(user_token):
			user_has_won = True
			return user_has_won

		
		#win_check(user_token)
	def computer_turn():
		computer_luck = random.randint(1,3)
		chance_dict = {}
		if computer_luck == 1:
			for item in board:
				if item != "X" or item != "Y":
					item_index = board.index(item)
					chance_dict[item] = item_index
			selection = random.choice(list(chance_dict.values()))
			for item in token:
				if token.index(item) == selection:
					token.index(item) = computer_token
		else:
			c_win = []
			for i in game_data["scores"]:
				inti = 0
				for base in i:
					if base == computer_token:
						inti += 1
				if inti > 0:
					c_win.append(base)
			choice = random.choice(c_win)
			token.index(choice) = computer_token
			if win_check(computer_token):
				computer_has_won = True
				return computer_has_won
	while 'true':
		if start == 1:
			player_turn()
		if start == 2:
			
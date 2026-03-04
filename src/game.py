#BH, KH, ZC 2nd game.py
import random
def game():
    print("Welcome to Tic-Tac-Toe!")
    token = input("Would you like to be X, or O? ").strip().upper()
    if token == "X":
        user_token = "X"
        computer_token = "O"
    else:
        user_token = "O"
        computer_token = "X"
    board = [str(i) for i in range(1, 10)]
    game_data = {
        "scores": {
            "win_1": [0, 1, 2],
            "win_2": [3, 4, 5],
            "win_3": [6, 7, 8],
            "win_4": [0, 3, 6],
            "win_5": [1, 4, 7],
            "win_6": [2, 5, 8],
            "win_7": [0, 4, 8],
            "win_8": [2, 4, 6]}}

    def print_board():
        print(f"{board[0]} {board[1]} {board[2]}")
        print(f"{board[3]} {board[4]} {board[5]}")
        print(f"{board[6]} {board[7]} {board[8]}")

    def win_check(symbol):
        for combo in game_data["scores"].values():
            a, b, c = combo
            if board[a] == board[b] == board[c] == symbol:
                return True
        return False

    def resetboard():
        return [i for i, vib in enumerate(board) if vib not in ("X", "O")]

    def player_turn():
        print_board()
        while True:
            try:
                choice = int(input("Please select the index of the square you choose (1–9): "))
            except ValueError:
                print("Please type a number between 1 and 9.")
                continue

            if choice < 1 or choice > 9:
                print("That is not a valid square.")
                continue

            idx = choice - 1
            if board[idx] in ("X", "O"):
                print("That square is already taken.")
                continue

            board[idx] = user_token
            break

        return win_check(user_token)

    def computer_turn():
        available = resetboard()
        if not available:
            return False
        idx = random.choice(available)
        board[idx] = computer_token
        print(f"Computer chooses square {idx + 1}")
        print_board()
        return win_check(computer_token)

    count = 0
    current = "player"

    while True:
        if not resetboard():
            print("It's a tie! No more moves left.")
            break

        if current == "player":
            if player_turn():
                count += 1
                print(f"You won! It took you {count} turns to defeat the computer.")
                break
            count += 1
            current = "computer"
        else:
            if computer_turn():
                count += 1
                print(f"The computer defeated you! It took {count} turns.")
                break
            current = "player"
    return count
game()
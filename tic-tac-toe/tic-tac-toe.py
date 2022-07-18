import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
game_running = True


# Game board
def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("___________")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("___________")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# Player input on board


def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if 1 <= inp <= 9 and board[inp - 1] == "-":  # change board to while as an experiment
        board[inp-1] = current_player
    elif board[inp-1] == "O":
        print("That place is already taken!")
        return player_input(board)


# check win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[7] == board[1] == board[4] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It is a tie")
        game_running = False


def check_win():
    global game_running
    if check_diagonally(board) or check_horizontal(board) or check_row(board):
        print_board(board)
        print(f"The winner is {winner}")
        game_running = False


def computer_player(board):
    position = random.randint(0,8)
    if board[position] == "-":
        board[position] = "O"
        switch_player()

# switch player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# check for win or tie again


while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer_player(board)
    check_win()
    check_tie(board)
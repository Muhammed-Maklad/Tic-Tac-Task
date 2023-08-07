import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True


def print_Board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_move(board):
    user_inputs = int(input("Enter number of box 1-9: "))
    if board[user_inputs-1] == "-":
        board[user_inputs-1] = currentPlayer
    else:
        print("there id player already here.")


def check_Col(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_Row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_Diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def check_Win(board):
    global gameRunning
    if check_Col(board) or check_Row(board) or check_Diagonal(board):
        print_Board(board)
        print(f"The winner is {winner}")
        gameRunning = False


def check_Tie(board):
    global gameRunning
    if "-" not in board:
        if (check_Col(board) or check_Row(board) or check_Diagonal(board)):
            pass
        else:
            print_Board(board)
            print("It is a tie")
            gameRunning = False


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    print_Board(board)
    player_move(board)
    check_Win(board)
    check_Tie(board)
    switchPlayer()
    if currentPlayer == "O":
        computer(board)
        check_Win(board)
        check_Tie(board)

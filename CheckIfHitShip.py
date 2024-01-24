from PlayersTurn import PlayerTurn
from Isallsunk import is_all_sunk

def check_hit(board, row, column, PlayerShips):
    while True:
        if board[row][column] != "":
            board[row][column] = "*"
            if is_all_sunk(PlayerShips):
                return "hI"
            PlayerTurn(board)
        if board[row][column] == "":
            board[row][column] = "!"  # miss
            return "."

board = [['.','.'],['.','.']]
row = 1
column = 1
PlayerShips = ["F", "F", "F", "F"]

print(check_hit(board, row, column, PlayerShips))

from InitialiseVariables import player1board_view, player2board_view, player1ships, player2ships
from PlaceShips import Choose_location

def PlayerTurn (Opp_Board, destroyer1, destroyer2, submarine1, submarine2, battleship1, battleship2, carrier1, carrier2):
    if Opp_Board == player1board_view:
        playerships = player1ships
        destroyer = destroyer1
        submarine = submarine1
        carrier = carrier1
        battleship = battleship1
    elif Opp_Board == player2board_view:
        playerships = player2ships
        destroyer = destroyer2
        submarine = submarine2
        carrier = carrier2
        battleship = battleship2

    print("Your turn. Enter a co-ordinate to hit")
    print(Opp_Board)

    row_index, column_index = Choose_location()
    check_hit(Opp_Board, row_index, column_index, destroyer, submarine, carrier, battleship)

def check_hit(board, row, column, destroyer, submarine, carrier, battleship):
    while True:
        if board[row][column] != "":
            board[row][column] = "*"  # opponent hits ship

            if is_all_sunk(destroyer, submarine, carrier, battleship):
                return "hI"

            if Is_Sunk(board, destroyer):
                if is_all_sunk():
                    print("Game over")
            if Is_Sunk(board, submarine):
                if is_all_sunk():
                    print("Game over")
            if Is_Sunk(board, carrier):
                if is_all_sunk():
                    print("Game over")
            if Is_Sunk(board, battleship):
                if is_all_sunk():
                    print("Game over")


            #PlayerTurn(board)
        if board[row][column] == "":
            board[row][column] = "!"  # miss
            break


def Is_Sunk(ship, board, player1ships):
    complete = 0
    for count in range(len(ship)):
        row = ship[count][0]
        column = ship[count][1]

def Is_Sunk(board, ship):
    complete = 0
    for count in range(len(ship)/2):
        row = ship[2*count-2]
        column = ship[2*count-1]

        if board[row][column] == "*":
            complete += 1
    if complete == len(ship):
        player1ships[0] == "F"
    return player1ships


def is_all_sunk(destroyer, submarine, carrier, battleship):
    if destroyer and submarine and carrier and battleship:
        return True
    else:
        return False



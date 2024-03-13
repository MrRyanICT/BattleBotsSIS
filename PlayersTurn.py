
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

    if board[row][column] != "":
        board[row][column] = "*"  # opponent hits ship
        destroyer = Is_Sunk(board, destroyer)
        if destroyer:
            if is_all_sunk():
                print("Game over")
        submarine = Is_Sunk(board, submarine)
        if submarine:
            if is_all_sunk():
                print("Game over")
        carrier = Is_Sunk(board, carrier)
        if carrier:
            if is_all_sunk():
                print("Game over")
        battleship = Is_Sunk(board, battleship)
        if battleship:
            if is_all_sunk():
                print("Game over")

        #PlayerTurn(board)
    if board[row][column] == "":
        board[row][column] = "!"  # miss
    return board

def Is_Sunk(board, ship):
    complete = 0
    for count in range(len(ship)/2):
        row = ship[count*2]
        column = ship[count*2 + 1]
        if board[row][column] == "*":
            complete += 1
    if complete == len(ship)/2:
        ship = True
        return ship
    return ship

def is_all_sunk(destroyer, submarine, carrier, battleship):
    if destroyer and submarine and carrier and battleship:
        return True
    else:
        return False



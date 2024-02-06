from CheckIfHitShip import check_hit
from InitialiseVariables import player1board_view, player2board_view, player1ships, player2ships
from PlaceShips import destroyer1, submarine1, carrier1, battleship1, destroyer2, submarine2, carrier2, battleship2, Choose_location

def PlayerTurn (Opp_Board):
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
    check_hit(Opp_Board, row_index, column_index, playerships, destroyer, submarine, carrier, battleship)

def check_hit(board, row, column, PlayerShips):
    while True:
        if board[row][column] != "":
            board[row][column] = "*"  # opponent hits ship
            if is_all_sunk(PlayerShips):
                return "hI"
            return False
            # PlayerTurn(board)
        if board[row][column] == "":
            board[row][column] = "!"  # miss
            return "."


PlayerTurn(player1board_view)

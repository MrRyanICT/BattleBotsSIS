#from CheckIfHitShip import check_hit
from InitialiseVariables import player1board_view, player2board_view, player1ships, player2ships
from ChangeToNumber import change
from PlaceShips import destroyer1, submarine1, carrier1, battleship1, destroyer2, submarine2, carrier2, battleship2

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

    print("Enter the row, 1-10")
    row = int(input())
    while row < 1 or row > 10:
        print('Error. Choose a number between 1 and 10')
        row = int(input())

    print("Enter the column, A-J. Capital letter please")   #I suggest using A-J
    column = input()
    column = changetonum(column)
    #check_hit(Opp_Board, row, column, playerships)

PlayerTurn(player1board_view)


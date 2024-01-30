from CheckIfHitShip import check_hit
from InitialiseVariables import player1board_view, player2board_view, player1ships, player2ships
from ChangeToNumber import changetonum

def PlayerTurn (Opp_Board):
    if Opp_Board == player1board_view:
        playerships = player1ships
    elif Opp_Board == player2board_view:
        playerships = player2ships

    print("Your turn. Enter a co-ordinate to hit")
    print(Opp_Board)
    while True:
        print("Enter the row, 1-10")
        row = int(input())
        if row < 1 or row > 10:
            print('Error. Choose a number between 1 and 10')
    print("Enter the column, A-J. Capital letter please")   #I suggest using A-J
    column = input()
    column = changetonum(column)
    check_hit(Opp_Board, row, column, playerships)

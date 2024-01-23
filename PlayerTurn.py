from Checkifhitship import check_hit

def PlayerTurn (Opp_Board):
    print("Your turn. Enter a co-ordinate to hit")
    print(Opp_Board)
    print("Enter the row, 1-10")
    row = input()
    print("Enter the column, 1-10")
    column = input()
    check_hit(Opp_Board, row, column)


from Checkifhitship import check_hit

def PlayerTurn (Opp_Board):
    print("Your turn. Enter a co-ordinate to hit")
    print(Opp_Board)
    while True:
        print("Enter the row, 1-10")
        row = int(input())
        if row < 1 or row > 10:
            print('Error. Choose a number between 1 and 10')
    print("Enter the column, 1-10")   #I suggest using A-J
    column = input()
    check_hit(Opp_Board, row, column)


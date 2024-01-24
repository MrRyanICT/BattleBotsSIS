def placeships(playerA,playerB):
    print('Place destroyer (2 boxes)')
    while True:
        row = int(input('Which row (Choose a number between 1-10)'))
        if row < 1 or row > 11:
            print('Error. Please choose a row between 1 and 10')
        else:
            break
        row_index = row - 1

    while True:
        column = input("Which Column? (Choose a CAPITAL letter between A-J)")
        if column < "A" or column > "J":
            print('Error. Please choose a column between A and J')
        else:
            break
        column_index = column - 1

def ConvertColumnToNumber(column:string):
    retrun ord(column) - 65

placeships(None,None)


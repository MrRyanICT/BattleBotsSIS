def placeships(playerA,playerB):
    print('Place destroyer (2 boxes)')
    while True:
        row = int(input('Which row (Choose a number between 1-10)'))
        if row < 1 or row > 11:
            print('Error. Please choose a row between 1 and 10')
        else:
            break

    while True:
        column = input("Which Column? (Choose a CAPITAL letter between A-J)")
        if column < "A" or column < "K":
            print('Error. Please choose a column between A and J')
        else:
            break


placeships(None,None)


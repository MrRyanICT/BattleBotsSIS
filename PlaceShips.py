from Utilities import CovertColumnToNumber

player1board = [['' for i in range(10)] for j in range(10)]
player2board = [['' for i in range(10)] for j in range(10)]
player1ships = ["Ship2", "Ship3", "Ship4", "Ship5"]
player2ships = ["Ship2", "Ship3", "Ship4", "Ship5"]
print(player1board)

def IllegalSpot(row_index, column_index, ship_size):
    if row_index + ship_size > 9 and column_index + ship_size > 9:
        return False
    else:
        return True

def Choose_location():
    while True:
        try:
            row = int(input('Which row (Choose a number between 1-10)'))
            if row < 1 or row > 11:
                print('Error. Please choose a row between 1 and 10')
            else:
                break
        except:
            print('Error. You need to enter a number')
    row_index = row - 1
    while True:
        column = input("Which Column? (Choose a CAPITAL letter between A-J)").upper()
        if column < "A" or column > "J":
            print('Error. Please choose a column between A and J')
        else:
            break
    column_index = CovertColumnToNumber(column)
    return row_index, column_index

def HorV(board, row_index, column_index, size, ship):
    is_free = True
    while True: #check if space is free or now
        orientation = input('You want to place it horizontally or vertically?. Type H or V').upper()
        while orientation != "H" and orientation != "V":
            print("STOP ERORR")
            orientation = input('You want to place it horizontally or vertically?. Type H or V').upper()
        if orientation == 'H':
            for counter in range(size):
                if not board[row_index][column_index + counter] == '':
                    is_free = False
                #board[row_index][column_index + counter] = "S"
        if orientation == "V":
            for counter in range(size):
                if not board[row_index][column_index + counter] == '':
                    is_free = False
                #board[row_index+  counter][column_index ] = "S"
        if not is_free:
            print('There\'s already a ship there. Go again')
            if size == 2:
                Placedestroyer(board)
            elif size == 3:
                Placesubmarine(board)
            elif size == 4:
                Placebattleship(board)
            elif size == 5:
                Placecarrier(board)
        else:
            break
    #write to board after validation
    if orientation == 'H':
        for counter in range(size):
            board[row_index][column_index + counter] = "S"
            ship.append(row_index, column_index)
    elif orientation == "V":
        for counter in range(size):
            board[row_index + counter][column_index] = "S"
            ship.append(row_index, column_index)
    return board

def Placedestroyer(board):
    print('Place a destroyer (2 boxes)')
    row_index, column_index = Choose_location()
    destroyer = []
    HorV(board, row_index, column_index, 2, destroyer)
    return board

def Placesubmarine(board):
    print('Place a submarine (3 boxes)')
    row_index, column_index = Choose_location()
    submarine = []
    HorV(board, row_index, column_index, 3, submarine)
    return board

def Placebattleship(board):
    print('Place a battleship (4 boxes)')
    row_index, column_index = Choose_location()
    battleship = []
    HorV(board, row_index, column_index, 4, battleship)
    return board

def Placecarrier(board):
    print('Place a battleship (5 boxes)')
    row_index, column_index = Choose_location()
    carrier = []
    HorV(board, row_index, column_index, 5, carrier)
    return board

#def checkboard(board):

print('Player 1 Choose your ships')
player1board = Placedestroyer(player1board)
player1board = Placesubmarine(player1board)
player1board = Placebattleship(player1board)
player1board = Placecarrier(player1board)
print(player1board)

#print('Player 2 Choose your ships')
#player2board = Placedestroyer(player2board)
#player2board = Placesubmarine(player2board)
#player2board = Placebattleship(player2board)
#player2board = Placecarrier(player2board)
#print(player2board)


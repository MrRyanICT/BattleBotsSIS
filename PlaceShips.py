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

def choose_location():
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

def shiptocall(size, board):
    if size == 2:
        placedestroyer(board)
    elif size == 3:
        placesubmarine(board)
    elif size == 4:
        placebattleship(board)
    elif size == 5:
        placecarrier(board)

def HorV(board, row_index, column_index, size):
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
            shiptocall(size, board)
        else:
            break
    #write to board after validation
    if orientation == 'H':
        for counter in range(size):
            board[row_index][column_index + counter] = "S"
    elif orientation == "V":
        for counter in range(size):
            board[row_index + counter][column_index] = "S"
    return board

def placedestroyer(board):
    print('Place a destroyer (2 boxes)')
    row_index, column_index = choose_location()
    HorV(board, row_index, column_index, 2)
    return board

def placesubmarine(board):
    print('Place a submarine (3 boxes)')
    row_index, column_index = choose_location()
    HorV(board, row_index, column_index, 3)
    return board

def placebattleship(board):
    print('Place a battleship (4 boxes)')
    row_index, column_index = choose_location()
    HorV(board, row_index, column_index, 4)
    return board

def placecarrier(board):
    print('Place a battleship (5 boxes)')
    row_index, column_index = choose_location()
    HorV(board, row_index, column_index, 5)
    return board

#def checkboard(board):

print('Player 1 Choose your ships')
player1board = placedestroyer(player1board)
player1board = placesubmarine(player1board)
#player1board = placebattleship(player1board)
#player1board = placecarrier(player1board)
print(player1board)

#print('Player 2 Choose your ships')
#player2board = placedestroyer(player2board)
#player2board = placesubmarine(player2board)
#player2board = placebattleship(player2board)
#player2board = placecarrier(player2board)
#print(player2board)


from InitialiseVariables import player1board, player2board, player2board_view, player1board_view
from PlayersTurn import PlayerTurn
from Isallsunk import is_all_sunk
from PlaceShips import IllegalSpot, Choose_location, HorV, Placedestroyer, Placesubmarine, Placebattleship, Placecarrier

def PlaceShipsPlayer1(board1):
    return board
    #this is a stub

def PlaceShipsPlayer2(board2):
    return board
    #this is a stub

print('Hi')
print("Battle Bots!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
board1 = PlaceShipsPlayer1(player1board)
board2 = PlaceShipsPlayer2(player2board)
print(player1board)
print(player2board)

print()
while not is_all_sunk:
    PlayerTurn(player2board_view)
    PlayerTurn(player1board_view)

from InitialiseVariables import player1board, player2board, player2board_view, player1board_view
from PlaceShips import setboard
from PlayersTurn import PlayerTurn

print('Hi')
print("Battle Bots!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
player1board, player2board = setboard(player1board, player2board)

while True:
    PlayersTurn(player2board_view)
    PlayersTurn(player1board_view)
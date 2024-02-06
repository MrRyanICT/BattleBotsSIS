from InitialiseVariables import player1board, player2board, player2board_view, player1board_view
from PlayersTurn import PlayerTurn
from PlaceShips import setboard

print('Hi')
print("Battle Bots!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
player1board, player2board = setboard()

print()
while not is_all_sunk:
    PlayerTurn(player2board_view)
    PlayerTurn(player1board_view)

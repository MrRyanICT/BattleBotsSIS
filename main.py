from InitialiseVariables import player1board, player2board, player2board_view, player1board_view
from PlaceShips import setboard
from PlayersTurn import PlayerTurn

print('Hi')
print("Battle Bots!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
player1board, player2board, destroyer1, destroyer2, submarine1, submarine2, battleship1, battleship2, carrier1, carrier2 = setboard(player1board, player2board)

while True:
    PlayerTurn(player2board_view, destroyer1, destroyer2, submarine1, submarine2, battleship1, battleship2, carrier1, carrier2)
    PlayerTurn(player1board_view, destroyer1, destroyer2, submarine1, submarine2, battleship1, battleship2, carrier1, carrier2)
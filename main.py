from InitialiseVariables import player1board, player2board, player2board_view, player1board_view
from PlaceShips import setboard
from PlayersTurn import PlayerTurn

print('Hi')
print("Battle Bots!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#player1board, player2board, destroyer1, destroyer2, submarine1, submarine2, battleship1, battleship2, carrier1, carrier2 = setboard(player1board, player2board)
player1board = [['S', 'S', '', '', '', '', '', '', '', ''], ['S', 'S', 'S', '', '', '', '', '', '', ''], ['S', 'S', 'S', 'S', '', '', '', '', '', ''], ['S', 'S', 'S', 'S', 'S', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '']]
player2board = [['S', 'S', '', '', '', '', '', '', '', ''], ['S', 'S', 'S', '', '', '', '', '', '', ''], ['S', 'S', 'S', 'S', '', '', '', '', '', ''], ['S', 'S', 'S', 'S', 'S', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '']]
destroyer1 = [0, 0, 0, 1]
destroyer2 = [0, 0, 0, 1]
submarine1 = [1, 0, 1, 1, 1, 2]
submarine2 = [1, 0, 1, 1, 1, 2]
battleship1 = [2, 0, 2, 1, 2, 2, 2, 3]
battleship2 = [2, 0, 2, 1, 2, 2, 2, 3]
carrier1 = [3, 0, 3, 1, 3, 2, 3, 3, 3, 4]
carrier2 = [3, 0, 3, 1, 3, 2, 3, 3, 3, 4]

while True:
    PlayerTurn(player2board_view, destroyer1, destroyer2, submarine1, submarine2, battleship1, battleship2, carrier1, carrier2)
    PlayerTurn(player1board_view, destroyer1, destroyer2, submarine1, submarine2, battleship1, battleship2, carrier1, carrier2)
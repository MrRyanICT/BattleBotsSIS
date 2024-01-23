from InitialiseVariables import player1board, player2board, player2board_view, player1board_view
from PlayerTurn import PlayerTurn
from Isallsunk import is_all_sunk

print("Battle Bots!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(player1board)
print(player2board)

print()
while not is_all_sunk:
    PlayerTurn(player2board_view)
    PlayerTurn(player1board_view)
from InitialiseVariables import player1board, player2board, player2board_view, player1board_view
from Player's Turn import PlayerTurn
from InitialiseVariables import player1board, player2board
print("Battle Bots!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(player1board)
print(player2board)

print()
while not is_all_sunk:
    PlayerTurn(Player1, player2board_view)
    PlayerTurn(Player2, player1board_view)
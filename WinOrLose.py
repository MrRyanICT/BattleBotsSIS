from Isallsunk import is_all_sunk
PlayerShipsA = ['F','F','F','F']

def winorlose():
    #A is true, B is false
    if is_all_sunk(PlayerShipsA):
        print('player A wins!')
    else:
        print('player B wins!')
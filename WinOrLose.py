PlayerShipsA = ['F','F','F','F']

def winorlose():
    #A is true, B is false
    if is_all_sunk(PlayerShipsA) == True:
        print('player A wins!')
    else:
        print('player B wins!')
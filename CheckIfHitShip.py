

def check_hit(board, row, column):
    hit = False
    if board[row][column] != "":
        hit = True
        board[row][column] = "*"
    else:
        board[row][column] = "!" #miss

    while hit:
        PlayerTurn(board)
        if board[row][column] != "":
            hit = True
            board[row][column] = "*"
        if board[row][column] == "":
            board[row][column] = "!"  # miss
            hit = False

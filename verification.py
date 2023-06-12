def verify(board: list[list[int]]) -> bool:
    # checking each row
    for row in board:
        data = {}
        for cell in row:
            if cell != 0:
                if data.get(cell) == None:
                    data.update({cell:1})
                else:
                    return False
    
    #checking each column
    col = 0
    while col < 9:
        data = {}

        for row in board:
            if row[col] != 0:
                if data.get(row[col]) == None:
                    data.update({row[col]: 1})
                else:
                    return False

        col += 1
    
    # checking each 3x3 blocks
    row_mul = 3
    for a in range(3):
        for i in range(3):
            data = {}
            for j in range(3):
                if board[i*row_mul][j + a*row_mul] != 0:
                    if data.get(board[i*row_mul][j + a*row_mul]) == None:
                        data.update({board[i*row_mul][j + a*row_mul]: 1})
                    else:
                        return False
                if board[i*row_mul + 1][j + a*row_mul] != 0:
                    if data.get(board[i*row_mul + 1][j + a*row_mul]) == None:
                        data.update({board[i*row_mul + 1][j + a*row_mul]: 1})
                    else:
                        return False
                if board[i*row_mul + 2][j + a*row_mul] != 0:
                    if data.get(board[i*row_mul + 2][j + a*row_mul]) == None:
                        data.update({board[i*row_mul + 2][j + a*row_mul]: 1})
                    else:
                        return False
    return True
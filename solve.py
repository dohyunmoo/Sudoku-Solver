def solve(board: list[list[int]]): 
    def valid_input(row, col, val):
        for i in range(9):
            if board[row][i] != 0 and board[row][i] == val: # check current row
                return False
            if board[i][col] != 0 and board[i][col] == val: # check current column
                return False

            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != 0 and board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == val: # check current 3x3 box
                return False
        return True

    def actual_solve():
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == 0:
                    for val in range(1, 10):
                        if valid_input(row, col, val):
                            board[row][col] = val
                            if actual_solve():
                                return True
                            else:
                                board[row][col] = 0
                    return False
        return True
    actual_solve()
   
    return board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8] 
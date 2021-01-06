# Sudoku solver using backtrack recursion
sudoku = [[5,3,0, 0,7,0, 0,0,0],
          [6,0,0, 1,9,5, 0,0,0],
          [0,9,8, 0,0,0, 0,6,0],

          [8,0,0, 0,6,0, 0,0,3],
          [4,0,0, 8,0,3, 0,0,1],
          [7,0,0, 0,2,0, 0,0,6],

          [0,6,0, 0,0,0, 2,8,0],
          [0,0,0, 4,1,9, 0,0,5],
          [0,0,0, 0,8,0, 0,7,9]]

def check(x, y, value, board):
    # Check vertical line
    for i in range(9):
        if(board[i][y] == value):
            return False
    # Check horizontal line
    for j in range(9):
        if(board[x][j] == value):
            return False
    # Check box
    x0 = 3*(x//3)
    y0 = 3*(y//3)
    for i in range(3):
        for j in range(3):
            if(board[x0+i][y0+j] == value):
                return False
    return True


def solve(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                for k in range(1, 10):
                    if(check(i, j, k, board)):
                        board[i][j] = k
                        solve(board)
                        board[i][j] = 0
                return
    show(board)

def show(board):
    for i in range(9):
        for j in range(9):
            print(f'{board[i][j]} ', end='')
            if((j+1)%3==0):
                print(' ', end='')
        print('\n', end='')
        if((i+1)%3==0 and i!=8):
            print('\n', end='')

solve(sudoku)
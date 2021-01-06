# Sudoku solver using backtrack recursion

# Example with an unique solution.
sudoku = [[5,3,0, 0,7,0, 0,0,0],
          [6,0,0, 1,9,5, 0,0,0],
          [0,9,8, 0,0,0, 0,6,0],

          [8,0,0, 0,6,0, 0,0,3],
          [4,0,0, 8,0,3, 0,0,1],
          [7,0,0, 0,2,0, 0,0,6],

          [0,6,0, 0,0,0, 2,8,0],
          [0,0,0, 4,1,9, 0,0,5],
          [0,0,0, 0,8,0, 0,7,9]]

# Check if a empty cell (x, y) can hold a certain number (value).
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

# Find all the possible solutions recursively.
def solve(board):
    # We could do some pruning, maybe pass the last cell changed,
    # so we can iterate starting from it.
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0): # if cell is empty
                for k in range(1, 10): # try every possible value
                    if(check(i, j, k, board)): # solve it recursively
                        board[i][j] = k
                        solve(board)
                        board[i][j] = 0
                return
    show(board)
    input()

# Show the sudoku board.
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

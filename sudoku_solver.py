# This program solves a sudoku by backtracking and filling all possible spaces.

def solve(board):
    empty = find_empty(board)

    if empty == None:
        return True
    else:
        x, y = empty

    for i in range(1,10):
        if check_validity(board, x, y, i):
            board[y][x] = i

            if solve(board):
                return True

            board[y][x] = 0

    return False

# This function Prints a Sudoku Board
def printb(board):
    for x in range(len(board)):
        if x % 3 == 0:
            print('-------------------------')
        for y in range(len(board[x])):
            if y % 3 == 0:
                print('|', end=' ')
            print(board[x][y], end=' ')
        print('|')
    print('-------------------------')


# This function checks if a passed number in a set of coordinates in valid.
def check_validity(board, x, y, num):
    # Check horizontal
    for i in range(len(board)):
        if board[y][i] == num and x != i:
            return False

    # Check vertical
    for i in range(len(board)):
        if board[i][x] == num and y != i:
            return False

    # Check square
    sqr_x = (x // 3) * 3
    sqr_y = (y // 3) * 3

    for i in range(sqr_y, sqr_y + 3):
        for j in range(sqr_x, sqr_x + 3):
            if board[i][j] == num and (i, j) != (y, x):
                return False

    return True


# This function finds the first empty square in the Sudoku.
def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 0:
                return x, y
    return None

# printb(board)
# starttime = time.time()
# solve(board)
# print('\n--------------------------\n')
# printb(board)
# print('\nIt took us ' + str(round(time.time() - starttime)) + ' seconds to solve the sudoku.')

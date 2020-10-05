from copy import deepcopy


def check_valid(bo, position, num):
    """
    :param bo: (int 2D Array) Sudoku Board
    :param position: (tuple) row, column
    :param num: (int) Inserted value
    :return: (bool) True is board state is valid. False if board state is not valid

    Check if the state of the board is valid for given input number at given position in the Sudoku Board
    """

    # Check validity in row
    for col in range(len(bo[0])):
        if bo[position[0]][col] == num and position[1] != col:
            return False

    # Check validity in column
    for row in range(len(bo)):
        if bo[row][position[1]] == num and position[0] != row:
            return False

    # Check validity in mini-square
    for row in range(position[0] // 3 * 3, (position[0] // 3 + 1) * 3):
        for col in range(position[1] // 3 * 3, ((position[1] // 3) + 1) * 3):
            if bo[row][col] == num and position != (row, col):
                return False

    return True


def print_board(b):
    """
    :param b: (int 2D Array) Sudoku Board
    :return: None
    """
    # Print Board to console
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print('|', end=" ")
            if j == 8:
                print(b[i][j])
            else:
                print(b[i][j], end=" ")


def find_empty(bo):
    """
    :param bo: (int 2D Array) Sudoku Board
    :return: (tuple) Row, Column

    Find position of first empty cell in Sudoku Board, Left -> Right, Top -> Bottom
    """
    # Find first empty position in the board
    # Left -> Right
    # Top -> Bottom
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column
    return None


def solve_board(bo):
    """
    :param bo: (int 2D Array) Sudoku Board
    :return: (bool) True - Solved, False - Not Solved

    Recursive backtracking algorithm used to solve the Sudoku Board
    """
    # Check if board is solved
    pos = find_empty(bo)
    if not pos:
        return True
    else:
        row, col = pos

    # Check for values 1-9
    for i in range(1, 10):
        if check_valid(bo, pos, i):
            bo[row][col] = i

            if solve_board(bo):
                return True

            bo[row][col] = 0

    return False


def solvable(bo):
    """
    :param bo: (int 2D Array) Game Board
    :return: (bool) True -> Solution available, False -> No solution for current Game Board

    Checks whether a game board has a solution or not
    """
    board = deepcopy(bo)
    # copy.deepcopy() copies values
    # copy.copy() --Shallow Copy-- copies references
    pos = find_empty(board)
    if not pos:
        return True
    else:
        row, col = pos

    # Check for values 1-9
    for i in range(1, 10):
        if check_valid(board, pos, i):
            board[row][col] = i

            if solvable(board):
                return True

            board[row][col] = 0

    return False

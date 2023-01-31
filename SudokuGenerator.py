from random import randint
from SudokuSolver import SudokuSolver

BOARD_SIZE = 9

board = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]
]


def generate_sudoku_board(sudoku_type=9):
    f"""
    Uses Backtracking algorithm to generate a valid sudoku board
    :return: array of arrays, valid sudoku board of size {BOARD_SIZE}
    """
    new_board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for val in range(1, BOARD_SIZE + 1):
        while True:
            # Get a random position from board
            row = randint(0, BOARD_SIZE - 1)
            col = randint(0, BOARD_SIZE - 1)
            # If the position is empty add the value to that position, else roll for a new position
            if new_board[row][col] == '.':
                new_board[row][col] = val
                break

    # Use backtracking to complete the board
    solver_obj = SudokuSolver(sudoku_board=new_board, generating=True)
    solver_obj.backtrack_solve_board()
    return solver_obj.get_board()

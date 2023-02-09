from random import randint
from SudokuSolver import SudokuSolver
from os import listdir
# import pprint

BOARD_SIZE = 9


def generate_backtrack_board(sudoku_type=9):
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

    print(solver_obj)
    return solver_obj.get_board()


def generate_board(sudoku_type=9):
    board_count = len(listdir("Sudoku_Grids/"))
    # print(available_boards_count)

    # If no boards are found in Sudoku_Grids/ generate a new one using **backtracking** algorithm
    if board_count > 0:
        board_id = f"grid_{randint(1, board_count):04d}.txt"
        # print(board_id)

        # Open txt file from board_id
        sudoku_board = [[]] * 9
        try:
            with open(f"Sudoku_Grids/{board_id}", "r") as grid:
                grid_lines = grid.readlines()

            for i in range(len(grid_lines)):
                # Will be needed if the last row in the txt file does not end with '\n'
                # if i == len(grid_lines) - 1:
                #     sudoku_board[i] = list(map(int, grid_lines[i].split(',')))
                #     continue
                
                # Exclude '\n' character in .txt file
                sudoku_board[i] = list(map(int, grid_lines[i][:-1].split(',')))

            # pprint.pprint(sudoku_board)
            return sudoku_board
        except OSError:
            pass

    return generate_backtrack_board(sudoku_type)

from random import randint

DIFFICULTY = {
    9: {'easy': 35, 'medium': 30, 'hard': 25, 'extreme': 20}
}


class SudokuSolver:
    def __init__(self, sudoku_board, level):
        self.game_board = sudoku_board
        # print(self.game_board)
        self.prep_board(DIFFICULTY[9][level])

    def prep_board(self, difficulty_level):
        # Calculate empty cells
        empty_cells = (len(self.game_board) ** 2) - difficulty_level
        for _ in range(empty_cells):
            while True:
                pos_row = randint(0, (len(self.game_board) - 1))
                pos_col = randint(0, (len(self.game_board) - 1))
                if self.game_board[pos_row][pos_col] == 0:
                    continue
                self.game_board[pos_row][pos_col] = 0
                break

    def __str__(self):
        # Overriding __str__ attribute allows to directly print SudokuSolver object using print()
        # prints game board to console
        board_console = ""
        for row in range(len(self.game_board)):
            if row % 3 == 0 and row != 0:
                board_console += "- - - - - - - - - - - \n"
            for col in range(len(self.game_board[0])):
                if col % 3 == 0 and col != 0:
                    board_console += "| "
                board_console += f"{self.game_board[row][col]} "
            board_console += "\n"
        return board_console

    def check_valid(self, position, value):
        # This function is designed for a 9x9 Sudoku board and will break if used for 4x4 or 6x6 sudoku boards
        pos_row, pos_col = position

        # Check containing column for matching value
        for col in range(len(self.game_board[0])):
            if self.game_board[pos_row][col] == value:
                return False

        # Check containing row for matching value
        for row in range(len(self.game_board)):
            if self.game_board[row][pos_col] == value:
                return False

        # Check containing block for matching element
        block_row = pos_row // 3
        block_col = pos_col // 3
        for i in range(3):
            for j in range(3):
                if self.game_board[(block_row * 3) + i][(block_col * 3) + j] == value:
                    return False

        # If the value is present in either of the three conditions, the function will have returned False
        # If the function is still running, the value is a valid entry for that cell
        return True

    def get_empty(self):
        # Will return the position of an empty cell in the sudoku board as a tuple
        # Returns None if no cells are empty
        for row in range(len(self.game_board)):
            for col in range(len(self.game_board[0])):
                if self.game_board[row][col] == 0:
                    return row, col
        return None

    def backtrack_solve_board(self):
        # Recursive solver using backtracking algorithm
        empty_cell = self.get_empty()
        # print(f"empty cell -> {empty_cell}")
        # Base condition
        if empty_cell:
            row, col = empty_cell
        else:
            return True

        for val in range(1, (len(self.game_board) + 1)):
            if self.check_valid(empty_cell, val):
                self.game_board[row][col] = val

                if self.backtrack_solve_board():
                    return True

                self.game_board[row][col] = 0
        # print("Resetting cell")
        return False

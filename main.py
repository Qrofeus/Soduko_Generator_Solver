from SudokuGenerator import generate_sudoku_board
from SudokuSolver import SudokuSolver  # DIFFICULTY

if __name__ == '__main__':
    difficulty_level = 'easy'
    sudoku_type = 9
    # while True:
    #     difficulty_level = input("Select your difficulty level\n[Easy, Medium, Hard, Extreme]: ").lower()
    #     if difficulty_level not in DIFFICULTY[sudoku_type].keys():
    #         print(">> Invalid input, try again")
    #         continue
    #     break

    sudoku_solver = SudokuSolver(sudoku_board=generate_sudoku_board(sudoku_type), level=difficulty_level,
                                 s_type=sudoku_type)
    print(sudoku_solver)

    print("Solving Sudoku puzzle...")
    sudoku_solver.backtrack_solve_board()
    print(sudoku_solver)

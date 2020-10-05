from Sudoku_Console import print_board, solve_board, solvable
from Sudoku_Questions import get_board, get_board_raw

# Driver Function
if __name__ == '__main__':
    while True:
        diff = str(input("Difficulty Level:\n")).lower()
        if diff == "easy" or diff == "medium" or diff == "hard":
            break

    if str(input("raw board / new board :: ")).lower() == "raw":
        curr_board = get_board_raw(diff)
    else:
        print("\nGenerating Game Board...")
        while True:
            curr_board = get_board(diff)
            if solvable(curr_board):
                break

    print()
    print_board(curr_board)
    print("\nSolving...")
    solve_board(curr_board)
    print("\nCompleted Board -->\n")
    print_board(curr_board)

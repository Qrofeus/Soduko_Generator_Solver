from random import randint
from Sudoku_Console import check_valid

boards = [
    [[4, 3, 5, 2, 6, 9, 7, 8, 1], [6, 8, 2, 5, 7, 1, 4, 9, 3], [1, 9, 7, 8, 3, 4, 5, 6, 2],
     [8, 2, 6, 1, 9, 5, 3, 4, 7], [3, 7, 4, 6, 8, 2, 9, 1, 5], [9, 5, 1, 7, 4, 3, 6, 2, 8],
     [5, 1, 9, 3, 2, 6, 8, 7, 4], [2, 4, 8, 9, 5, 7, 1, 3, 6], [7, 6, 3, 4, 1, 8, 2, 5, 9]],
    [[7, 8, 5, 4, 3, 9, 1, 2, 6], [6, 1, 2, 8, 7, 5, 3, 4, 9], [4, 9, 3, 6, 2, 1, 5, 7, 8],
     [8, 5, 7, 9, 4, 3, 2, 6, 1], [2, 6, 1, 7, 5, 8, 9, 3, 4], [9, 3, 4, 1, 6, 2, 7, 8, 5],
     [5, 7, 8, 3, 9, 4, 6, 1, 2], [1, 2, 6, 5, 8, 7, 4, 9, 3], [3, 4, 9, 2, 1, 6, 8, 5, 7]]
]


# get play Board
def get_board_raw(difficulty):
    """
    :param difficulty: (String) "easy, "medium", "hard"
    :return: (int 2D Array) Game Board

    Selects a random board and initializes with random input
    """
    q_board = [[0 for row in range(9)] for col in range(9)]
    board = boards[randint(0, len(boards) - 1)]
    row, col, val = 0, 0, 30

    # Select difficulty level
    if difficulty == "easy":
        val = 30
    elif difficulty == "medium":
        val = 20
    elif difficulty == "hard":
        val = 10

    # Generate Game Board
    for i in range(val):
        while True:
            row = randint(0, 8)
            col = randint(0, 8)
            if q_board[row][col] == 0:
                break

        q_board[row][col] = board[row][col]

    return q_board


def get_board(difficulty):
    """
    :param difficulty: (String) "easy, "medium", "hard"
    :return: (int 2D Array) Game Board

    Selects a random board and initializes with random input
    """
    # "easy" difficulty tends to take *a lot* of time to generate board from scratch
    q_board = [[0 for row in range(9)] for col in range(9)]
    row, col, val = 0, 0, 30

    # Select difficulty level
    if difficulty == "easy":
        val = 30
    elif difficulty == "medium":
        val = 20
    elif difficulty == "hard":
        val = 10

    # Generate Game Board
    for i in range(val):
        while True:
            while True:
                row = randint(0, 8)
                col = randint(0, 8)
                if q_board[row][col] == 0:
                    break
            num = randint(1, 9)
            if check_valid(q_board, (row, col), num):
                q_board[row][col] = num
                break

    return q_board

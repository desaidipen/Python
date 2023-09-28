import datetime


def solve_sudoku(board):
    # Find the next empty cell
    empty_cell = find_empty_cell(board)

    # If there are no empty cells, the puzzle is solved
    if not empty_cell:
        return True

    row, col = empty_cell

    # Try filling the empty cell with numbers from 1 to 9
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num

            # Recursively try to solve the puzzle
            if solve_sudoku(board):
                return True

            # If the puzzle can't be solved with this number, backtrack
            board[row][col] = 0

    # If no number can be placed, backtrack to the previous cell
    return False


def find_empty_cell(board):
    # Find the first empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


def is_valid_move(board, row, col, num):
    # Check if the number is not in the same row, column, or 3x3 box
    return (
        not used_in_row(board, row, num)
        and not used_in_col(board, col, num)
        and not used_in_box(board, row - row % 3, col - col % 3, num)
    )


def used_in_row(board, row, num):
    return num in board[row]


def used_in_col(board, col, num):
    return num in [board[row][col] for row in range(9)]


def used_in_box(board, start_row, start_col, num):
    for row in range(3):
        for col in range(3):
            if board[row + start_row][col + start_col] == num:
                return True
    return False


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    # Example Sudoku puzzle as a 9x9 grid (0 represents empty cells)
    # puzzle = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]

    puzzle = [
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 0, 0, 0, 4, 6, 1, 0, 8],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 5, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 8, 0, 9, 4, 0, 0],
        [1, 0, 0, 3, 5, 0, 0, 0, 0],
        [2, 0, 4, 0, 8, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    start = datetime.datetime.now()
    if solve_sudoku(puzzle):
        print("Solved Sudoku Puzzle:")
        print_board(puzzle)
    else:
        print("No solution exists.")
    end = datetime.datetime.now()
    print("Time to Solve: {0}".format(end - start))

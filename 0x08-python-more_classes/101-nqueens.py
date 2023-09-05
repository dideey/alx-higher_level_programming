#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list): The chessboard represented as a list of lists.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen; False otherwise.
    """
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N queens problem and return all possible solutions.

    Args:
        n (int): The size of the board.

    Returns:
        list: A list of solutions, each represented as a list of strings.
    """
    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()


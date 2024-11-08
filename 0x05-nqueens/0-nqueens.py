#!/usr/bin/python3
import sys


def print_usage_and_exit(message):
    """Prints a message and exits the program."""
    print(message)
    sys.exit(1)


def solve_nqueens(n):
    """Solves the N Queens problem and prints all solutions."""
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        """Checks if a queen can be placed at (row, col) without conflict."""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def place_queen(row):
        """Tries to place queens row by row and saves solutions."""
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                place_queen(row)
                board[row] = -1

    place_queen(0)
    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solve_nqueens(N)

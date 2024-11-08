#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    solutions = []
    board = [-1] * N

    def place_queen(row):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                place_queen(row + 1)
                board[row] = -1  # Reset the board to backtrack

    place_queen(0)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

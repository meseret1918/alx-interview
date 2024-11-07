#!/usr/bin/python3
"""
Solution to the N Queens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Backtracking function to find all solutions for the N Queens problem.

    Args:
        r (int): Current row to place the queen.
        n (int): Size of the chessboard (N x N).
        cols (set): Set to track columns where queens are placed.
        pos (set): Set to track positive diagonals where queens are placed.
        neg (set): Set to track negative diagonals where queens are placed.
        board (list): 2D list representing the chessboard.

    This function prints each solution as a list of queen coordinates.
    """
    if r == n:
        # Collect and print solution when all queens are placed
        res = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 1:
                    res.append([row, col])
        print(res)
        return

    for c in range(n):
        # Check if the position is safe
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place queen
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Move to the next row
        backtrack(r + 1, n, cols, pos, neg, board)

        # Backtrack: remove the queen
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Sets up the board and initiates the backtracking to solve the N Queens problem.

    Args:
        n (int): The number of queens and the size of the chessboard (N x N).
    """
    cols = set()      # Tracks columns with queens
    pos_diag = set()  # Tracks positive diagonals with queens
    neg_diag = set()  # Tracks negative diagonals with queens
    board = [[0] * n for _ in range(n)]  # Initialize N x N chessboard

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate that N is a positive integer of at least 4
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Solve the N Queens problem
    nqueens(n)

#!/usr/bin/python3
"""
Solution to the N-Queens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Backtrack function to find solutions to the N-Queens problem.

    Args:
        r (int): The current row.
        n (int): The size of the board (number of queens).
        cols (set): A set of columns that are already occupied by a queen.
        pos (set): A set of positive diagonals that are already occupied.
        neg (set): A set of negative diagonals that are already occupied.
        board (list): The current board state, with 1's indicating queens.

    Returns:
        None: This function prints each valid solution.
    """
    if r == n:
        res = []
        for row in range(len(board)):  # Renamed 'l' to 'row'
            for col in range(len(board[row])):  # Renamed 'k' to 'col'
                if board[row][col] == 1:
                    res.append([row, col])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place the queen
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Recursively place the next queen
        backtrack(r + 1, n, cols, pos, neg, board)

        # Backtrack
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        n (int): The number of queens to place on the board.
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]  # Create an n x n board

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    # Validate arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

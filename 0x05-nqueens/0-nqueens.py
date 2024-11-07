#!/usr/bin/python3
"""
<<<<<<< HEAD
Solution to the nqueens problem
=======
Solution to the N-Queens problem
>>>>>>> 95abd2462f14fb89d6fce54467ce6e88984ed4fd
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
<<<<<<< HEAD
    """
    backtrack function to find solution
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
=======
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
>>>>>>> 95abd2462f14fb89d6fce54467ce6e88984ed4fd
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

<<<<<<< HEAD
=======
        # Place the queen
>>>>>>> 95abd2462f14fb89d6fce54467ce6e88984ed4fd
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

<<<<<<< HEAD
        backtrack(r+1, n, cols, pos, neg, board)

=======
        # Recursively place the next queen
        backtrack(r + 1, n, cols, pos, neg, board)

        # Backtrack
>>>>>>> 95abd2462f14fb89d6fce54467ce6e88984ed4fd
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
<<<<<<< HEAD
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
=======
    Solve the N-Queens problem and print all possible solutions.

    Args:
        n (int): The number of queens to place on the board.
>>>>>>> 95abd2462f14fb89d6fce54467ce6e88984ed4fd
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
<<<<<<< HEAD
    board = [[0] * n for i in range(n)]
=======
    board = [[0] * n for _ in range(n)]  # Create an n x n board
>>>>>>> 95abd2462f14fb89d6fce54467ce6e88984ed4fd

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
<<<<<<< HEAD
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
=======
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
>>>>>>> 95abd2462f14fb89d6fce54467ce6e88984ed4fd

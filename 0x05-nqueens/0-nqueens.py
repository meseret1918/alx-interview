#!/usr/bin/python3
"""
Solution to the N Queens problem.
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
        board (list): List of queen positions for the current solution.
        
    This function prints each solution as a list of queen coordinates.
    """
    if r == n:
        print(board)
        return

    for c in range(n):
        # Check if the position is safe
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place queen and add to tracking sets
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board.append([r, c])

        # Recur to place the next queen
        backtrack(r + 1, n, cols, pos, neg, board)

        # Backtrack: remove the queen and update tracking sets
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board.pop()


def nqueens(n):
    """
    Sets up the board and initiates the backtracking to solve the N Queens problem.

    Args:
        n (int): The number of queens and the size of the chessboard (N x N).
    """
    backtrack(0, n, set(), set(), set(), [])


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate that N is an integer and at least 4
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

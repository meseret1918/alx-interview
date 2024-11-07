#!/usr/bin/python3
"""
Solution to the N Queens problem.
"""
import sys


def solve_nqueens(n):
    """
    Solves the N Queens problem and prints all solutions.
    
    Args:
        n (int): Size of the chessboard and the number of queens to place.
    """
    solutions = []
    board = []
    cols = set()
    pos_diags = set()  # Row + Column (positive diagonals)
    neg_diags = set()  # Row - Column (negative diagonals)

    def backtrack(row):
        if row == n:
            # Found a valid solution, add a copy to the solutions list
            solutions.append(board[:])
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
                continue

            # Place the queen
            cols.add(col)
            pos_diags.add(row + col)
            neg_diags.add(row - col)
            board.append([row, col])

            # Move to the next row
            backtrack(row + 1)

            # Remove the queen and backtrack
            cols.remove(col)
            pos_diags.remove(row + col)
            neg_diags.remove(row - col)
            board.pop()

    # Start the backtracking from the first row
    backtrack(0)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Validate the input
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(n)

#!/usr/bin/python3
import sys

def print_solutions(board):
    """Print the board configuration."""
    print(board)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == row - r:
            return False
    return True

def solve_nqueens(n, row, board):
    """Solve the N queens problem using backtracking."""
    if row == n:
        print_solutions(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board)
            board[row] = -1  # Backtrack

def main():
    """Main function to solve the N queens problem."""
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

    # Initialize the board (-1 means no queen placed in that row)
    board = [-1] * n
    solve_nqueens(n, 0, board)

if __name__ == "__main__":
    main()

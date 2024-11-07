#!/usr/bin/python3
import sys

def print_solutions(solutions):
    """Prints each solution in the required format"""
    for solution in solutions:
        print(solution)

def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N, board, col, solutions):
    """Uses backtracking to find all solutions"""
    if col == N:
        solution = [[i, board[i].index(1)] for i in range(N)]
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(N, board, col + 1, solutions) or res
            board[i][col] = 0  # Backtrack

    return res

def nqueens(N):
    """Sets up the board and initiates the backtracking"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(N, board, 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Ensure N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Ensure N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    nqueens(N)

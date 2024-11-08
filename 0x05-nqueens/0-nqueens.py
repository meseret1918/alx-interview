#!/usr/bin/python3
<<<<<<< HEAD
import sys


def print_usage_and_exit(message):
    """Prints a message and exits the program."""
    print(message)
    sys.exit(1)


def solve_nqueens(n):
    """Solves the N Queens problem and prints all solutions."""
    solutions = []
    board = [-1] * n
=======
"""
Solution to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    backtrack function to find solution
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return
>>>>>>> eb3117b536d7081c47fa2954b154e37fa7812f00

    def is_safe(row, col):
        """Checks if a queen can be placed at (row, col) without conflict."""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

<<<<<<< HEAD
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
=======
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
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
>>>>>>> eb3117b536d7081c47fa2954b154e37fa7812f00

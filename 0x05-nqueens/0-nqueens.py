#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard.

Usage: nqueens N
"""
import sys


def solve_n_queens(n):
    """
    Solves the N queens puzzle challenge
    Keyword arguments:
    n - number of non-attacking queens in nxn chessboard
    Return: list of possible solutions
    """
    col = set()
    posDiag = set()  # row + column
    negDiag = set()  # row - column

    results = []
    board = [["."] * n for _ in range(n)]  # Chessboard

    def backtrack(r):
        """"Backtracking recursive function"""
        if r == n:
            copy = ["".join(row) for row in board]
            results.append(copy)  # Append valid solution
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return results


def print_n_queens(solutions):
    """Prints the coordinates of possible solutions"""
    solution = []
    for i in range(len(solutions)):
        for j in range(len(solutions[i])):
            for k in range(len(solutions[i][j])):
                if solutions[i][j][k] == "Q":
                    solution.append([j, k])
        print(solution)
        solution.clear()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)
    print_n_queens(solve_n_queens(n))

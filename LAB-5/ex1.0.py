def solve_n_queens(n):
    def is_not_under_attack(board, row, col):
        for i in range(row):
            if board[i][col]:
                return False
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j]:
                return False
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j]:
                return False
        return True

    def place_queen(board, row):
        if row == n:
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_not_under_attack(board, row, col):
                board[row][col] = True
                place_queen(board, row + 1)
                board[row][col] = False

    solutions = []
    board = [[False] * n for _ in range(n)]
    place_queen(board, 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join('Q' if cell else '.' for cell in row))
        print()

def main():
    n = 8
    solutions = solve_n_queens(n)
    print(f"Total number of solutions: {len(solutions)}")
    print("Solutions:")
    print_solutions(solutions)

if __name__ == "__main__":
    main()

def solve_n_queens(n):
    # Helper function to check if a queen can be placed at (row, col)
    def is_not_under_attack(board, row, col):
        # Check the column for another queen
        for i in range(row):
            if board[i][col]:
                return False
        # Check the major diagonal for another queen
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j]:
                return False
        # Check the minor diagonal for another queen
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j]:
                return False
        return True

    # Helper function to place queens using backtracking
    def place_queen(board, row):
        if row == n:
            # If all queens are placed successfully, add the solution
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_not_under_attack(board, row, col):
                board[row][col] = True  # Place the queen
                place_queen(board, row + 1)  # Move to the next row
                board[row][col] = False  # Remove the queen (backtrack)

    solutions = []  # List to store all valid solutions
    board = [[False] * n for _ in range(n)]  # 2D array to represent the board
    place_queen(board, 0)  # Start placing queens from the first row
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            # Construct a string for each row of the board
            # 'Q' if the column index has a queen, otherwise '.'
            print(' '.join('Q' if cell else '.' for cell in row))
        print() # Print a newline between different solutions

def main():
    n = 8  # Number of queens (and size of the board)
    solutions = solve_n_queens(n)
    print(f"Total number of solutions: {len(solutions)}")
    print("Solutions:")
    print_solutions(solutions)

if __name__ == "__main__":
    main()

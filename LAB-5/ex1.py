def solve_n_queens(n):
    # Helper function to check if a queen can be placed at (row, col)
    def is_not_under_attack(row, col):
        for prev_row in range(row):
            # Check columns and diagonals for attacks
            if queens[prev_row] == col or \
               queens[prev_row] - prev_row == col - row or \
               queens[prev_row] + prev_row == col + row:
                return False
        return True

    # Helper function to place queens using backtracking
    def place_queen(row):
        if row == n:
            # If all queens are placed successfully, add the solution
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_not_under_attack(row, col):
                queens[row] = col  # Place the queen
                place_queen(row + 1)  # Move to the next row
                # No need to reset queens[row] because it will be overwritten

    solutions = []  # List to store all valid solutions
    queens = [-1] * n  # Array to store the column positions of queens
    place_queen(0)  # Start placing queens from the first row
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            # Construct a string for each row of the board
            # 'Q' if the column index matches the queen's position, otherwise '.'
            print(' '.join('Q' if i == row else '.' for i in range(len(solution))))
        print() # Print a newline between different solutions

def main():
    n = 8  # Number of queens (and size of the board)
    solutions = solve_n_queens(n)
    print(f"Total number of solutions: {len(solutions)}")
    print("Solutions:")
    print_solutions(solutions)

if __name__ == "__main__":
    main()

def solve_n_queens(n):
    def is_not_under_attack(row, col):
        for prev_row in range(row):
            if queens[prev_row] == col or \
               queens[prev_row] - prev_row == col - row or \
               queens[prev_row] + prev_row == col + row:
                return False
        return True

    def place_queen(row):
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_not_under_attack(row, col):
                queens[row] = col
                place_queen(row + 1)

    solutions = []
    queens = [-1] * n
    place_queen(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join('Q' if i == row else '.' for i in range(len(solution))))
        print()

def main():
    n = 8
    solutions = solve_n_queens(n)
    print(f"Total number of solutions: {len(solutions)}")
    print("Solutions:")
    print_solutions(solutions)

if __name__ == "__main__":
    main()

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

N = int(input("Enter size of board (N): "))

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQueen(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueen(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

# Initialize the board with 0s
board = [[0 for _ in range(N)] for _ in range(N)]

# Call the main function
if solveNQueen(board, 0) == True:
    print("Solution exists:")
    printSolution(board)
else:
    print("No solution exists.")
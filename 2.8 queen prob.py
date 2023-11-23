def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    for row in range(8):
        line = ""
        for col in range(8):
            line += "Q" if board[row] == col else "."
        print(line)
    print()

def solve_queens(board, row):
    if row == 8:
        print_solution(board)
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1)
            board[row] = -1  # backtrack

if __name__ == "__main__":
    # Initialize the board with -1 indicating an empty cell
    board = [-1] * 8
    solve_queens(board, 0)

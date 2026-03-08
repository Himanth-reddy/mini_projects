import requests
response = requests.get("https://sudoku-api.vercel.app/api/dosuku")
board = response.json()["newboard"]["grids"][0]["value"]
'''solve(board):
    find empty cell
    if none → solved

    try numbers 1..9
        if valid
            place number
            solve again
            if solved → return
            remove number

    return failure '''

def solve(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row , col = empty_cell
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board , num , row, col):
    for i in range(len(board)):
        if board[i][col] == num:
            return False
    for j in range(len(board[0])):
        if board[row][j] == num:
            return False
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()


if solve(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:    
    print("No solution exists")
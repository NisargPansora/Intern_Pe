import random

def create_board():
    return [[" "] * 7 for _ in range(6)]

def print_board(board):
    print("-" * 21)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-" * 21)

def is_valid_move(board, col):
    return board[0][col] == " "

def get_next_open_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == " ":
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    for c in range(4):
        for r in range(6):
            if board[r][c:c+4] == [piece] * 4:
                return True
    for c in range(7):
        for r in range(3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    for c in range(4):
        for r in range(3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
            if all(board[r+3-i][c+i] == piece for i in range(4)):
                return True
    return False

def get_valid_moves(board):
    return [col for col in range(7) if is_valid_move(board, col)]

def play_game():
    board = create_board()
    print_board(board)
    turn = 0

    while True:
        col = int(input("Player 1, choose a column (0-6): ")) if turn == 0 else random.choice(get_valid_moves(board))
        if not is_valid_move(board, col):
            print("Invalid move. Try again.")
            continue

        row = get_next_open_row(board, col)
        drop_piece(board, row, col, "X" if turn == 0 else "O")
        print_board(board)

        if winning_move(board, "X" if turn == 0 else "O"):
            print("Player 1 wins!" if turn == 0 else "Computer wins!")
            break
        elif not get_valid_moves(board):
            print("It's a draw!")
            break

        turn = 1 - turn

play_game()
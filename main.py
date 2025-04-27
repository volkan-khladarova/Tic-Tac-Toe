# Initializing the game board
def print_board(board):
    print("\n") # Add new line for better formatting
    for i in range(3):
        print(" | ".join(board[i])) # Print each row, joining elements whit " | "
        if i < 2:
            print("---------") # Print separators between rows, except after the last row
    print("\n") # Add new line for better formatting

board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 grid with empty spaces

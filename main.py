# Initializing the game board
def print_board(board):
    print("\n") # Add new line for better formatting
    for i in range(3):
        print(" | ".join(board[i])) # Print each row, joining elements whit " | "
        if i < 2:
            print("---------") # Print separators between rows, except after the last row
    print("\n") # Add new line for better formatting

# Checking for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        # Check horizontal rows
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True # Return True if there's a horizontal winner
        # Check vertical rows
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True # Return True if there's a vertical winner
        # Check diagonal rows
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True # Return True if there's a diagonal winner (top-left to bottom-right)
        if board[0][2] == board[1][1] == board[2][0] == player:
            return  True  # Return True if there's a diagonal winner (top-right to bottom-left)
        return False # Return False if no winner

# Check for a draw
def check_draw(board):
    for row in board: # Iterate through each row of the board
        for cell in row: # Iterate through each cell in the row
            if cell == " ": # If there's an empty cell, return False (game isn't over)
                return False
    return True # If no empty cells are left, return True (it's a draw)


board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 grid with empty spaces

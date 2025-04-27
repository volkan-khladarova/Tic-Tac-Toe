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

# Check if the move is valid
def valid_move(board, move):
    if move < 1 or move > 9: # Check if the move is between 1 and 9
        return False # Return False if the move is out of range
    row, col = divmod(move - 1, 3)  # Convert the move (1-9) to row and column (0-2)
    return board[row][col] == " " # Return True if the chosen cell is empty

# Make the move and update the board
def make_move(board, move, player):
    row, col = divmod(move - 1, 3)  # Convert the move (1-9) to row and column (0-2)

    # If the cell is already occupied, it's an invalid move
    if board[row][col] in ["X", "O"]:
        return False  # Return False if the cell is already occupied

    board[row][col] = player  # Set the chosen cell to the current player's symbol
    return True  # Return True to indicate the move was successful

# Main game loop
def play_game():
    # Get player names
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")
    # Start with an empty board
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]  # Initialize a 3x3 grid with empty spaces

    # The first player is X
    current_player = "X"  # Set the first player to X

    # The loop continues until the game is over
    game_over = False # Set a flag to track the game status

    while not game_over: # Keep looping until the game is over
        # Print the current state of the board
        print_board(board)

        # Prompt the user to make a move
        if current_player == "X":
            move = int(input(f"{player1}'s turn (X), enter your move (1-9): "))  # Get Player 1's move
        else:
            move = int(input(f"{player2}'s turn (O), enter your move (1-9): "))  # Get Player 2's move

        # Check if the move is valid
        if not valid_move(board, move):
            print("Invalid move. Please try again.") # If the move is invalid, ask the player to try again
            continue # Skip the rest of the loop and prompt the user again

        # Make the move on the board
        make_move(board, move, current_player)

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                print(f"{player1} wins!")  # Announce Player 1 as the winner
            else:
                print(f"{player2} wins!")  # Announce Player 2 as the winner
            game_over = True  # End the game

board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 grid with empty spaces

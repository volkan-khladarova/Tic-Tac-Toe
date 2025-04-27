class TicTacToe:
    def __init__(self):
        # Initialize the game state
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]  # Create a 3x3 board with numbers from 1-9
        self.current_player = "X"  # Player "X" starts the game
        self.game_over = False  # Game state flag, initially set to False (game is not over)

    # Function to print the current game board
    def print_board(self):
        print("\n")  # Print a newline for better formatting
        for i in range(3):  # Loop through each row of the board
            print(" | ".join(self.board[i]))  # Join each cell with " | " to print the row in a readable format
            if i < 2:  # If it's not the last row
                print("---------")  # Print a separator between rows
        print("\n")  # Print a newline for better formatting

# Check for a draw
def check_draw(board):
    # Check if there are any numbers (1-9) left on the board
    for row in board:  # Iterate through each row of the board
        for cell in row:  # Iterate through each cell in the row
            if cell not in ["X", "O"]:  # If the cell is a number (empty space), it's not a draw yet
                return False  # Return False if the game is not over (there are still numbers left)
    return True  # Return True if no numbers are left, indicating a draw


# Check if the move is valid
def valid_move(board, move):
    if move < 1 or move > 9: # Check if the move is between 1 and 9
        return False # Return False if the move is out of range
    row, col = divmod(move - 1, 3)  # Convert the move (1-9) to row and column (0-2)
    return board[row][col] not in ["X", "O"] # Return True if the chosen cell is empty

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

        # Check if the game ended in a draw
        elif check_draw(board):
             print_board(board)
             print("It's a draw!")  # Declare the draw
             game_over = True  # End the game

        # Switch players
        current_player = "O" if current_player == "X" else "X"  # Switch between X and O


# Start the game
if __name__ == "__main__":
    play_game() # Call the play_game function to start the game
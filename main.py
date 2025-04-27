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

    # Function to check if the current player has won
    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):  # Check each row
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current_player:
                return True  # Return True if a horizontal winner is found
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current_player:
                return True  # Return True if a vertical winner is found
        # Check both diagonals for a winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return True  # Return True if a diagonal winner is found (top-left to bottom-right)
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True  # Return True if a diagonal winner is found (top-right to bottom-left)
        return False  # Return False if no winner is found

    # Function to check if the game has ended in a draw
    def check_draw(self):
        # Check if there are any numbers (1-9) left on the board, meaning the game isn't finished
        for row in self.board:
            for cell in row:
                if cell not in ["X", "O"]:  # If a cell still contains a number
                    return False  # The game isn't over yet
        return True  # If all cells are filled, it's a draw

    # Function to validate if a player's move is valid
    def valid_move(self, move):
        # Check if the move is within the range 1-9
        if move < 1 or move > 9:
            return False  # Return False if the move is out of bounds
        row, col = divmod(move - 1, 3)  # Convert the move (1-9) to row and column indexes (0-2)
        return self.board[row][col] not in ["X", "O"]  # Return True if the cell is not occupied by "X" or "O"

    # Function to make a move and update the board
    def make_move(self, move):
        # Convert the move (1-9) to row and column indexes (0-2)
        row, col = divmod(move - 1, 3)
        self.board[row][col] = self.current_player  # Place the current player's symbol ("X" or "O") on the board

    # Function to switch to the next player
    def switch_player(self):
        # Switch between players "X" and "O"
        self.current_player = "O" if self.current_player == "X" else "X"

    # Main game loop that handles the gameplay
    def play_game(self):
        # Ask for player names
        player1 = input("Enter name for Player 1 (X): ")
        player2 = input("Enter name for Player 2 (O): ")

        # Loop until the game is over
        while not self.game_over:
            self.print_board()  # Print the current state of the board

            # Prompt the current player to enter their move
            if self.current_player == "X":
                move = int(input(f"{player1}'s turn (X), enter your move (1-9): "))  # Player 1's turn
            else:
                move = int(input(f"{player2}'s turn (O), enter your move (1-9): "))  # Player 2's turn

            # Check if the move is valid, and ask for a valid move if it's not
            if not self.valid_move(move):
                print("Invalid move. Please try again.")  # Notify the player if the move is invalid
                continue  # Skip the rest of the loop and prompt the player again

            # Make the move on the board
            self.make_move(move)

            # Check if the current player has won
            if self.check_winner():
                self.print_board()  # Print the final board
                winner = player1 if self.current_player == "X" else player2  # Determine the winner based on the symbol
                print(f"{winner} wins!")  # Announce the winner
                self.game_over = True  # Set the game state to over
            # Check if the game has ended in a draw
            elif self.check_draw():
                self.print_board()  # Print the final board
                print("It's a draw!")  # Announce the draw
                self.game_over = True  # Set the game state to over
            else:
                self.switch_player()  # Switch to the next player for the next turn

        # Switch players
        current_player = "O" if current_player == "X" else "X"  # Switch between X and O

# To start the game
if __name__ == "__main__":
    game = TicTacToe()  # Create an instance of the TicTacToe class
    game.play_game()  # Start the game by calling the play_game method

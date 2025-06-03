"""
External Modules:
- random: Python standard library used for generating the computer's moves.
"""
import random


class Board:
    """
    Creates the board and displays it.
    """
    def __init__(self):
        """
        Initializes an empty 3x3 Tic Tac Toe board.
        Each cell in the grid is set to a blank space.
        """
        self.grid = [" " for _ in range(9)]

    def display_board(self):
        """
        Prints the current board layout to the console in a formatted 3x3 grid.
        Includes dividing lines for visual clarity.
        """
        print()
        for row in range(3):
            i = row * 3
            print(f" {self.grid[i]} | {self.grid[i+1]} | {self.grid[i+2]} ")
            if row < 2:
                print("---|---|---")
        print()


def welcome_message():
    """
    Displays the welcome message and instructions to the player.
    Prompts the player to confirm if they want to start the game.
    Returns True if the player agrees to start, False otherwise.
    """
    print("Welcome to Tic Tac Toe!")
    print("Your goal is to align three 'X' symbols before the computer "
          "aligns three 'O'.")
    print("Choose a number between 1 and 9 to place your 'X'. "
          "The board positions are numbered like this:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 \n")
    while True:
        start_the_game = input("Are you ready to play ? (y/n):").lower()
        if start_the_game == 'y' or start_the_game == 'yes':
            print("Now here is the board, let's play!\n")
            return True
        elif start_the_game == 'n' or start_the_game == 'no':
            print('See you soon then!')
            return False
        else:
            print("Please enter 'y' or 'n'.")


def get_player_input(board):
    """
    Prompts the player to enter a move.
    Ensures the input is a number between 1 and 9 and that the chosen cell is
    empty. Converts the input to 0-based index for internal use.
    Repeats until a valid move is entered.
    """
    while True:
        try:
            move = int(input("Enter a number between 1 and 9: "))
            if move < 1 or move > 9:
                print('That number is out of range. Please enter a number '
                      'between 1 and 9.')
            elif board.grid[move - 1] != " ":
                print('This spot is already taken. Try again')
            else:
                return move - 1
        except ValueError:
            print('Not a number. Please enter a number between 1 and 9.')


def get_computer_input(board):
    """
    Generates a valid move for the computer.
    Randomly selects a position between 0 and 8 until an empty cell is found.
    """
    while True:
        computer_move = random.randint(0, 8)
        if board.grid[computer_move] == " ":
            return computer_move


def check_win(board):
    """
    Checks if either the player or the computer has won the game.
    Evaluates all possible winning combinations on the board.
    If a win is detected, prints the winner and returns True.
    """
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                        [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for combo in win_combinations:
        if (
            board.grid[combo[0]] == board.grid[combo[1]] ==
            board.grid[combo[2]] == 'X'
        ):
            print('You won!')
            return True
        elif (
            board.grid[combo[0]] == board.grid[combo[1]] ==
            board.grid[combo[2]] == 'O'
        ):
            print('The computer won :(')
            return True
    return False


def check_draw(board):
    """
    Checks if the game has ended in a draw.
    A draw occurs when all cells on the board are filled and there is
    no winner.
    """
    if " " not in board.grid:
        print("It's a draw!")
        return True
    return False


def play_game(board):
    """
    Manages the main game loop for a single round of Tic Tac Toe.
    Alternates turns between the player and the computer.
    Updates the board after each move.
    The game continues until a player wins or the board is full,
    resulting in a draw.
    """
    while True:
        print("Computer's turn:")
        computer_move = get_computer_input(board)
        board.grid[computer_move] = 'O'
        print(f"Computer chose: {computer_move + 1}")
        board.display_board()
        if check_win(board):
            break
        elif check_draw(board):
            break

        print("Your turn:")
        move = get_player_input(board)
        board.grid[move] = 'X'
        print(f"Player chose: {move + 1}")
        board.display_board()
        if check_win(board):
            break


def play_again():
    """
    Asks the player if they want to play another round of Tic Tac Toe.
    Continuously prompts the user until a valid answer ('y' or 'n') is
    received.
    Returns True if the user wants to play again, and False otherwise.
    """
    while True:
        answer = input('Do you want to play again? Type y for yes or n for '
                       'no :').lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            print('Thank you for playing tic tac toe with us!')
            return False
        else:
            print("Please enter 'y' or 'n'.")


def main():
    """
    Run all program functions
    """
    if not welcome_message():
        return

    while True:
        board = Board()
        play_game(board)
        if not play_again():
            break


main()

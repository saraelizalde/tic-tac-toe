import random

class Board :
    """
    Creates the board and displays it.
    """
    def __init__(self):
        self.grid = [" " for _ in range(9)]

    def display_board(self):
        print()
        for row in range(3):
            i= row * 3
            print(f" {self.grid[i]} | {self.grid[i+1]} | {self.grid[i+2]} ")
            if row < 2:
                print("---|---|---")
        print()

def get_player_input(board):
    while True:
        try:
            move = int(input("Enter a number between 0 and 8: "))
            if move > 8 or move < 0:
                print('Number out of range. Try again')
            elif board.grid[move] != " ":
                print('This box is already taken. Try again')
            else:              
                return move
        except ValueError:
            print("Not a number. Try again")

def get_computer_input(board):
    while True:
        computer_move = random.randint(0, 8)
        if board.grid[computer_move] == " ":
            return computer_move

def check_win(board):   
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in win_combinations:
        if board.grid[i[0]] == board.grid[i[1]] == board.grid[i[2]] == 'X':
            print('You won !')
            return True
        elif board.grid[i[0]] == board.grid[i[1]] == board.grid[i[2]] == 'O':
            print('The computer won :(')
            return True
    return False

            







def main():
    """
    Run all program functions
    """
    board = Board()
    board.display_board()
    move = get_player_input(board)
    board.grid[move] = 'X'
    print(f"Player chose: {move}")
    board.display_board()
    computer_move = get_computer_input(board)
    board.grid[computer_move] = 'O'
    print(f"Computer chose: {computer_move}")
    board.display_board()
    if check_win(board):
        return
main()

        
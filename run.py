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

    


def main():
    """
    Run all program functions
    """
    board = Board()
    board.display_board()
    move = get_player_input(board)
    print(f"Player chose: {move}")

main()

        
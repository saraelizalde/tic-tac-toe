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


def main():
    """
    Run all program functions
    """
    board = Board()
    board.display_board()

main()

        
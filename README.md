
# Tic Tac Toe

Tic Tac Toe is a Python terminal game where the player and computer take turns placing X and O, aiming to align three symbols in a row, column, or diagonal to win.

 ?? Here is a link to the live version of the project.

## How to play

When you run the program, you’ll be greeted with a welcome message explaining the objective and layout of the Tic Tac Toe board. Your goal is to place three of your symbols (‘X’) in a row — horizontally, vertically, or diagonally — before the computer places three of its symbols (‘O’).

1. Start the Game: You’ll be asked if you're ready to play. Enter y or yes to begin, or n or no to exit.

2. Making a Move: On your turn, enter a number between 0 and 8 to place your ‘X’ on the board. The numbers correspond to board positions shown during the initial instructions.

3. Computer’s Turn: After your move, the computer will automatically choose an available position to place its ‘O’.

4. Board Updates: After each move (yours and the computer’s), the current state of the board will be displayed.

5. Win or Draw Check: After every turn, the game checks if either player has aligned three of their symbols. If so, the winner is announced. If the board is full with no winner, it's a draw.

6. Play Again: After the game ends, you’ll be asked if you want to play again. Enter y or yes to play another round. If you enter n or no, the game will exit.



## Features

### Existing features

- 3x3 Board Display:  
A visual representation of the Tic Tac Toe board is displayed in the terminal, updating after each move.
- Computer Opponent:  
The computer selects a random valid move using Python’s built-in random library, making the game playable in single-player mode.
- User Input Handling:  
The player is prompted to input a number between 0 and 8 to select a position on the board.
- Input Validation and Error Handling:  
The game checks that the user input is:  
   - A number
   - Within the valid range (0–8)
   - On an empty spot  
   If the input is invalid, a helpful message is displayed, and the user is asked to try again.

### Futur features
 
- ??
- ??
- ??

## Data Model

The application uses a simple object-oriented data model centered around a Board class. This class manages the state and display of the 3x3 Tic Tac Toe grid:

- self.grid: A one-dimensional Python list of 9 elements representing the board cells. Each index (0–8) corresponds to a specific position on the board, allowing for straightforward data manipulation and win/draw checks.

- display_board(): A method that prints the current state of the board in a visually understandable 3x3 format, helping players see the game progression.

By encapsulating board-related data and logic inside a class, the program maintains cleaner separation of concerns and supports easier updates or extensions in the future.

## Testing

I have manually tested this project by doing the following: 

- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected and non-empty spots
- Tested in my local terminal and the Code Institute Heroku terminal

### Bugs

- ??
- ??

### Remaining Bugs

- ??
- ??

### Validator Testing

- PEP8
   - No errors were returned from PEP8online.com

## Development

- I started by planning the flow of my code on paper. I outlined which functions I would need and in what order they should run. This helped me ensure the code would be structured and logical before writing it. Planning ahead also helped me avoid bugs and made the code easier to reuse and maintain.
- I decided to create a Board class to manage the game board. It includes an __init__ method to initialize the board and a display_board method to print it. After some trial and error, I realized I needed to structure the methods carefully so the board wouldn't reset after each move. I added formatting with side and bottom separators to improve readability, and I used a condition to avoid adding a line under the last row to keep the layout symmetrical.
- I created the main function to call and run all the other functions. At first, I struggled to see any output on the console because I forgot to create an instance of the Board class. Once I instantiated the board correctly, the game board appeared as expected.
- Next, I created the get_player_input function, which includes error handling and checks to ensure the input is a number between 0 and 8. Initially, I tried to update the board inside this function using self.grid[move] = 'X', but that didn’t work because I was referencing self without being inside the class. I realized I needed to use board.grid[move] = 'X' instead. I also moved this line into the main function so that it could properly access the player's input and update the board.
- For the get_computer_input function, I imported the random module from Python’s standard library. I used random.randint(0, 8) to generate a random number between 0 and 8, simulating the computer's move. The function loops until it finds an empty spot on the board to ensure the computer doesn’t pick an already occupied cell.
- For the check_win function, I initially wrote a basic condition to detect a win, like checking if the first row was all Xs. But that led to repetitive code. To simplify it, I created a list of all winning combinations and looped through them. I struggled at first to match these combinations with the correct board positions. Eventually, I removed the unnecessary while True loop and used return True when a winning condition was met, and return False if none were.
- I then wrote the play_game function to handle turn-taking between the player and the computer. It runs in a loop until someone wins or the game ends in a draw. To keep the game flow organized, I moved some function calls—like getting player input, updating the board, and checking for a win or draw—from main into play_game. This made the main function cleaner and kept the game logic all in one place.
- I then wrote the check_draw function to detect when the game ends in a draw (when all spaces on the board are filled and no one has won). After creating it, I added a call to check_draw inside the play_game function, right after checking for a win, so the game can correctly end and inform the player when there's no winner.
- While writing the play_again function, I ran into a problem where the game kept asking if I wanted to play again, even when I said no. This happened because I was calling main() from inside play_again(), which created a new loop every time and never exited properly. I tried calling play_game() instead, and while it exited correctly on "no," it didn’t restart the game properly since the board wasn’t reset. I considered resetting the board inside play_again(), but decided a better solution was to structure a loop inside main() and use play_again() only to return True to restart or False to exit. This way, the game could restart cleanly without nested function calls.

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku

- Step for deployment:
   - Fork or clone this repository
   - Create a new Heroku app
   - Set the buildbacks to Python and NodeJS in that order
   - Set config vag to: key: PORT and value: 8000
   - Link the Heroku app to the repository
   - Click on Deploy

- Here is the link to the deployed website: 
- Here is the link to the github repository:

## Credits

- ??
- ??

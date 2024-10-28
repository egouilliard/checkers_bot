# Checkers

## Members:
- Adonnis Ortiz : GUI
- Erin Matthews :TUI
- Edouard Gouilliard : Game Logic
- Federico Guglielmotti : BOT

## Milestone 2 Feedback:
- Move all functions specific to checkers to game class
- Board class should be easily portable to another game like chess
- Explain why we have a separate player class
- Commit requirements.txt to github repo
- Prompt user for board size before creating it
- Implement ability to take multiple pieces in one move

## TUI
- Current implementation includes 
    - Board display
    - Piece display
    - Board size logic is implemented 
- Changes
    - Added functionality to request user input to create a board of size n*2+2
    - Added AssertionErrors


## Running the GUI
> Note that this requires an installation of *pygame* to your environment

To run the GUI, run the following command from the terminal 

                   python3 GUI.py


- Input the board size as requested into the terminal
- Enjoy the game

__*Revisions to the code*__
> Implemented support for the is_king parameter
>
> Implemented player support 
>
> Game logic has been applied
> > Piece implementation, piece movement, and game rules
> 
> Addition of the GUIgame class
>  > adding support for more Checkers_ed.py functionality

__*To Impove*__
> Completely define, turn based logic, and player specific turn rules for the game
> 
> Define the winner withint the pygame window
> 
> GUI/HCI functionality that would improve user experience
> > Turn display
> > 
> > Squares to which the piece can move can be highlighted
> > 
> > Smoother implementation and collection of board size

## Running the Game Logic:

Going through the basics:
1. This must be done through ipython3
2. There are two colors, BLACK and RED
3. To access the color BLACK you can type Piece.BLACK
4. To access the color RED you can type Piece.RED

Creating a Player:
1. Player1=Player(Piece.RED)
2. Player2=Player(Piece.BLACK)

Creating a Board:
1. Board=Board(n) where n is how many rows of pieces you want the board to have.

You must have numpy installed to run the Game Logic. To do run the following:
1. pip install numpy

To play or test the Game manually:
1. Create your players (player1 and player2) and Board
2. Create the game with your players and Board Two Options to play the game:
3. Either play the Game like you would in the Connect4 example or play using Game.play()

## Running the Bot:
1. Create instance of SmarterBot using parameters from the game that the bot
  should suggest moves for.
2. Run method .suggest_move() on this instance

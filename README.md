# Checkers

## Overview
This repository contains a Checkers game implementation with both a Text User Interface (TUI) and a Graphical User Interface (GUI). It also includes a chess bot that can suggest moves for the game.

## Installation
To install the necessary dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

### TUI
- Current implementation includes 
    - Board display
    - Piece display
    - Board size logic is implemented 
- Changes
    - Added functionality to request user input to create a board of size n*2+2
    - Added AssertionErrors

### Running the GUI
To run the GUI, run the following command from the terminal:

```
python3 GUI.py
```

- Input the board size as requested into the terminal
- Enjoy the game

### Running the Game Logic

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

### Running the Bot
1. Create an instance of SmarterBot using parameters from the game that the bot should suggest moves for.
2. Run the method `.suggest_move()` on this instance.

## Contributing
If you would like to contribute to this repository, please follow these guidelines:
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Submit a pull request with a clear description of your changes

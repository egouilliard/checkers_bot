import numpy as np
import checkers_ed

class TUI:
    """
    Class for TUI
    """
    def __init__(self, board, player1, player2):
        """
        Constructor.

        Parameters:
        - board (Object): Board object
        - player1 (Object): First player
        - player2 (Object): Second player

        """
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def game_text(self):
        """
        TUI for checkers
        """
        self.player1.color = checkers_ed.Piece.BLACK
        self.player2.color = checkers_ed.Piece.RED

        board_size = input("What size board do you want to play with? Please \
                           input a number n that will be the number of rows of \
                           pieces each player has.")
        
        new_board = checkers_ed.Board(board_size)
        self.board = new_board

        while not self.board.is_winner():
            #Print the board
            print(self.board)

            #Ask the current player which piece they want to move from a list
            movable_pieces = {k: v for k, v in \
                              self.current_player.legal_moves.items() if v}
            movable_locs = movable_pieces.keys()
            print("These are the pieces you can currently move:", movable_locs)
            sel_piece = input("Which piece would you like to move?")

            #Display the possible moves for that piece
            sel_piece_moves = self.current_player.legal_moves[sel_piece]
            print("These are the locations you can move that piece to:", \
                  sel_piece_moves)

            #Ask the player where they want to move the piece
            sel_move = input("Where would you like to move it?")

            #Move the piece
            self.board.move_piece(sel_piece, sel_move)

            #Switch players
            self.board.change_player()

        #Print the winner and resulting board
        print(self.board)
        if self.is_winner == self.player1:
            print("Player 1 wins!")
        if self.is_winner == self.player2:
            print("Player 2 wins!")

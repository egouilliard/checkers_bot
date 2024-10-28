"""
CMSC 14200, Winter 2023
Project

People Consulted:
    List anyone (other than the course staff) that you consulted about
    this assignment.
Online resources consulted:
    List the URLs of any online resources other than the course text and
    the official Python language documentation that you used to complete
    this assignment.

    1) To create a board, you would use the "Board class" to create a
    board object.

    board1 = Board(3)

    2)The player class contains a dictionary that contains each legal move
    for their pieces within the board. The dictionary is made up of the
    key: being the piece, and the value: being a list of tuples.

    self.legal_moves[piece name]

    -given the list that this returns, then you can see where you can move.

    3) self.legal_moves[piece name]

    4) for i in self.legal_moves.itmes()
        print(i)

    5) To check for the winner if len(self.remaining pieces) == 0 or if
        self.legal_moves is empty.

    """
import numpy as np

class Player:
    """
    Class representing a player.
    """

    def __init__(self, color):
        """
        Constructor

        Parameters:
        - color (str): color of the piece,"RED" or "BLACK"
        - legal moves (dict): keys are pieces, values are list of possible moves for that piece.
        """
        self.color = color
        self.forfeit = False
        raise NotImplementedError

    def __str__(self):
        if self.color == Piece.RED:
            return "R"
        elif self.color == Piece.BLACK:
            return "B"

class Piece:
    """
    Class representing a piece.
    """
    BLACK='BLACK'
    RED='RED'

    def __init__(self,color,position):
        """
        Constructor.
        Parameters:
        - color (str): color of the piece,"White" or "Black"
        - position (tuple): tuple of format (row (int),col (int)) 
        _ symbol (None or str): symbol or piece or if not a piece None
        """
        self.color=color
        self.position=position
        self.is_king = False
        raise NotImplementedError

    def __str__(self):
        if self.color == Piece.RED:
            return "R"
        elif self.color == Piece.BLACK:
            return "B"
    
    def __eq__(self, other):
        if not isinstance(other, Piece):
            return False
        return self.color == other.color

class Board:
    """
    Class for representing the Checkers board.
    """

    def __init__(self, n):
        """
        Constructor.

        Parameters:
        - n (int): number of rows of pieces a player starts with to begin the game
        - board (list): list of lists
        """
        # Height and Width of board = 2*n+2
        self.dim=n*2+2
        self.board=[]
        for i in range(self.dim):
            row=[]
            for j in range(self.dim):
                if ((i % 2 == 1 and 0 == j % 2 ) or (i % 2 == 0 and 1 == j % 2)) and i <= n-1:
                    row.append(Piece(Piece.BLACK, (i,j)))
                elif ((i % 2 == 1 and 0 == j % 2 ) or (i % 2 == 0 and 1 == j % 2)) and i > self.dim-n-1:
                    row.append(Piece(Piece.RED, (i,j)))
                else:
                    row.append(None)
            self.board.append(row)
        raise NotImplementedError

    def __str__(self):
        #s = " -" * self.row + "\n"
        s="  "
        s+=' '.join(np.arange(self.dim).astype(str))+"\n"
        for i,row in enumerate(self.board):
            s+=str(i)
            for piece in row:
                if piece is None:
                    s += "| "
                else:
                    s += "|"+str(piece.__str__())
            s += "|"+"\n"
        return s

class Game:
    """
    Class handling game logic
    """
    def __init__(self, Board, player1, player2):
        """
        Constructor.

        Parameters:
        - board (Object): Board object
        - player1 (Object): First player
        - player2 (Object): Second player

        """
        self.Board=Board
        self.player1=player1
        self.player2=player2
        self.current_player=self.player1
        raise NotImplementedError

    def play(self):
        """
        Start game and alternate between players until
        game is over.
        """
        raise NotImplementedError
    def switch_player_turn(self):
        """
        Switching between player.

        Returns: nothing
        """
        raise NotImplementedError

    def get_all_pieces(self, color = None):
        """
        Gets a list of all the games piece on the board

        Parameters:
        - color 'optional' (str)):
                If color is given, return all
                pieces of that color.

        Returns: List of Piece objects on the board
        """
        raise NotImplementedError

    def remove_piece(self, piece):
        """
        Removes piece from the board.

        Parameters:
        - piece: Piece object

        Returns: updated board
        """
        raise NotImplementedError

    def is_game_over(self):
        """
        Returns the color of the winning player if the game is over,
        or None if the game is not over.
        """
        raise NotImplementedError

    def forfeit(self, player):
        """
        Forfeits the game for the given player.

        Parameters:
        - player (Object): Player object

        Returns: None
        """
        raise NotImplementedError

    def is_position_valid(self, position):
        """
        Checks if position is on the board

        Parameters:
        - position (Tuple): a tuple of the next postion in the form (row,col),
                    where row and col are integers.

        Returns: True if position is valid, False otherwise.
        """
        raise NotImplementedError

    def get_piece(self, position):
        """
        Get the piece at a given postion.

        Parameters:
        - position (tuple): a tuple with the form (row,col),
                    where row and col are integers

        Returns: The piece at the given position,
                 or None if there is no piece.
        """
        raise NotImplementedError

    def get_captured_piece(self, piece, destination):
        """
        Returns a list of all opposing pieces that would be captured by the given move.

        Parameters:
        - piece: Piece object
        - destination (Tuple): a tuple of the next postion in the form (row,col),
                    where row and col are integers.

        Returns: List of Piece objects that would be captured by the move, or an empty list
                if no pieces would be captured.
        """
        raise NotImplementedError

    def get_legal_moves(self, piece):
        """
        Returns a list of all legal moves for the given piece.

        Parameters:
        - piece: Piece object

        Returns: List of tuples of the form (row,col) representing the legal moves for the given piece.
        """
        raise NotImplementedError

    def get_all_legal_moves(self, color):
        """
        Returns a list of all legal moves for the given color.

        Parameters:
        - color (str): Color of the player

        Returns: Dictionary of all legal moves for all pieces on the board, grouped by player.
        """
        raise NotImplementedError

    def is_move_valid(self, piece, destination):
        """
        Checks if the given move is valid for the given piece.

        Parameters:
        - piece: Piece object
        - destination (Tuple): a tuple of the next postion in the form (row,col),
                       where row and col are integers.

        Returns: True if the move is valid, False otherwise.

        """
        raise NotImplementedError

    def move_piece(self, piece, next_position):
        """
        Moves the piece at the given position to the next position on the board.

        Parameters:
        - position (tuple): a tuple of the current position in the form (row, col),
                            where row and col are integers.
        - next_position (tuple): a tuple of the next position in the form (row, col),
                            where row and col are integers.

        Returns: updated board
        """
        raise NotImplementedError

    def _can_capture_piece(self, piece):
        """
        Checks if the given piece can capture an opposing piece.

        Parameters:
        - piece: Piece object

        Returns: True if the piece can capture, False otherwise.
        """
        raise NotImplementedError

    def can_capture_piece(self, player_color):
        """
        Returns True if the given player can capture an opponent's piece, False otherwise.

        Parameters:
        - player_color (str): the color of the player

        Returns: True if the player can capture an opponent's piece, False otherwise.
        """
        raise NotImplementedError
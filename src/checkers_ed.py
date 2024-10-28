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

    def play(self):
        """
        Start game and alternate between players until
        game is over.
        """
        # While the game is not over
        while self.is_game_over() == 'RED and BLACK are still playing!':
            # Print the board
            print(self.Board)
            # Get the piece to move
            piece_to_move = None
            while True:
                try:
                    input_str = input(f"{self.current_player.color}'s turn: Enter the position of the piece you want to move (row, col) or type 'forfeit' to forfeit the game: ")
                    if input_str.lower() == 'forfeit':
                        self.forfeit(self.current_player)
                        break
                    row, col = map(int, input_str.split(','))
                    print("Your piece position:", row, col)
                    piece_to_move = self.get_piece((row, col))
                    
                    if piece_to_move is None:
                        raise AssertionError("This is not your piece! Please choose a valid piece.")
                    if piece_to_move.color!=self.current_player.color:
                        raise AssertionError("Invalid piece! Please choose a valid piece.")
                    
                    drow, dcol = map(int, input(f"Enter the destination for the piece at {piece_to_move.position} (row, col): ").split(','))
                    print("Your destination postiion:", drow, dcol)
                    destination = (drow, dcol)

                    # Get all the legal moves for the piece
                    legal_moves = self.get_all_legal_moves(self.current_player.color)
                    if destination not in legal_moves[piece_to_move.position]:
                        raise AssertionError("Invalid move! Please choose a valid move.")
                    
                    # Check if the move resulted in a capture
                    captured_piece = self.get_captured_piece(piece_to_move, destination)
                    # Make the move
                    self.move_piece(piece_to_move, destination)
                    # Check if the move resulted in a king
                    if destination[0] == 0 or destination[0] == self.Board.dim-1:
                        piece_to_move.is_king = True

                    # Check if the move resulted in a capture
                    # and same piece can capture again
                    if captured_piece and self._can_capture_piece(piece_to_move):
                        self.remove_piece(captured_piece)
                        # Switch back to the same player's turn
                        self.switch_player_turn()
                    
                    # Switch to the other player's turn
                    self.switch_player_turn()
                    break
                except Exception as e:
                    print("Error:", e)
                    continue
        
    def switch_player_turn(self):
        """
        Switching between player.

        Returns: nothing
        """
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_all_pieces(self, color = None):
        """
        Gets a list of all the games piece on the board

        Parameters:
        - color 'optional' (str)):
                If color is given, return all
                pieces of that color.

        Returns: List of Piece objects on the board
        """
        if color is not None:
            return [piece for row in self.Board.board for piece in row if piece is not None and piece.color == color]
        else:
            return [piece for row in self.Board.board for piece in row if piece is not None]

    def remove_piece(self, piece):
        """
        Removes piece from the board.

        Parameters:
        - piece: Piece object

        Returns: updated board
        """
        # Base case
        if piece == None:
            return self.Board
        position = piece.position
        self.Board.board[position[0]][position[1]] = None
        return self.Board

    def is_game_over(self):
        """
        Returns the color of the winning player if the game is over,
        or None if the game is not over.
        """
        pieces1 = self.get_all_pieces(self.player1.color)
        pieces2 = self.get_all_pieces(self.player2.color)
        if len(pieces1) == 0:
            print(f"{self.player2.color} wins!")
            return f"{self.player2.color} wins!"
        elif len(pieces2) == 0:
            print(f"{self.player1.color} wins!")
            return f"{self.player1.color} wins!"
        elif self.player1.forfeit == True:
            print(f"{self.player2.color} wins!")
            return f"{self.player2.color} wins!"
        elif self.player2.forfeit == True:
            print(f"{self.player1.color} wins!")
            return f"{self.player1.color} wins!"
        else:
            return f"{self.player1.color} and {self.player2.color} are still playing!"

    def forfeit(self, player):
        """
        Forfeits the game for the given player.

        Parameters:
        - player (Object): Player object

        Returns: None
        """
        print(f"{player.color}: YOU LOSE!")
        player.forfeit = True

    def is_position_valid(self, position):
        """
        Checks if position is on the board

        Parameters:
        - position (Tuple): a tuple of the next postion in the form (row,col),
                    where row and col are integers.

        Returns: True if position is valid, False otherwise.
        """
        row, col = position
        if row < 0 or row >= self.Board.dim or col < 0 or col >= self.Board.dim:
            raise AssertionError("Position is not on the board")
        else:
            return True

    def get_piece(self, position):
        """
        Get the piece at a given postion.

        Parameters:
        - position (tuple): a tuple with the form (row,col),
                    where row and col are integers

        Returns: The piece at the given position,
                 or None if there is no piece.
        """
        # Check position is valid
        self.is_position_valid(position)
        row, col = position
        return self.Board.board[row][col]

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
        current_position = piece.position
        dy = destination[0] - current_position[0]
        dx = destination[1] - current_position[1]
        self.is_position_valid(destination)
        # Check if the move is a diagonal move
        if abs(dx) != abs(dy):
            raise AssertionError("Move is not diagonal")
        # Check if the move is in the correct direction
        if not piece.is_king:
            if piece.color == Piece.RED and dy > 0:
                raise AssertionError("Piece is not a king and is moving in the wrong direction")
            elif piece.color == Piece.BLACK and dy < 0:
                raise AssertionError("Piece is not a king and is moving in the wrong direction")
        # Check for captured piece along the diagonal
        captured_piece = None
        step_row = 1 if dy > 0 else -1
        step_col = 1 if dx > 0 else -1
        for i in range(1, max([abs(dx),abs(dy)])):
            row = current_position[0] + i * step_row
            col = current_position[1] + i * step_col
            diagonal_position = (row, col)
            try:
                self.is_position_valid(diagonal_position)
            except Exception:
                continue
            diagonal_piece = self.get_piece(diagonal_position)
            if diagonal_piece is not None and diagonal_piece.color != piece.color:
                if captured_piece is None:
                    captured_piece = diagonal_piece
                else:
                    # Can't capture multiple pieces in one move
                    raise AssertionError("Can't capture multiple pieces in one move")
        return captured_piece

    def get_legal_moves(self, piece):
        """
        Returns a list of all legal moves for the given piece.

        Parameters:
        - piece: Piece object

        Returns: List of tuples of the form (row,col) representing the legal moves for the given piece.
        """
        # Base case
        if piece is None:
            raise AssertionError("Piece is None")
        legal_moves = []
        row, col = piece.position
        # Check if piece is king or not
        if piece.is_king:
            # Check all diagonal directions for legal moves
            for i, j in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                new_row, new_col = row + i, col + j
                destination = (new_row, new_col)
                try:
                    destination = (new_row, new_col)
                    self.is_position_valid(destination)
                    self.is_move_valid(piece, destination)
                    legal_moves.append(destination)
                except Exception:
                    try:
                        destination = (new_row + i, new_col + j)
                        self.is_position_valid(destination)
                        self.is_move_valid(piece, destination)
                        captured_piece = self.get_captured_piece(piece, destination)
                        if captured_piece:
                            legal_moves.append(destination)
                    except Exception:
                        pass
                    try:
                        destination = (new_row + i, new_col - j)
                        self.is_position_valid(destination)
                        self.is_move_valid(piece, destination)
                        captured_piece = self.get_captured_piece(piece, destination)
                        if captured_piece:
                            legal_moves.append(destination)
                    except Exception:
                        pass
        else:
            # Check the two diagonal directions for legal moves
            move_direction = 1 if piece.color == Piece.BLACK else -1
            for i, j in [(move_direction, 1), (move_direction, -1)]:
                new_row, new_col = row + i, col + j
                destination = (new_row, new_col)
                try:
                    destination = (new_row, new_col)
                    self.is_position_valid(destination)
                    self.is_move_valid(piece, destination)
                    legal_moves.append(destination)
                except Exception:
                    try:
                        destination = (new_row + i, new_col + j)
                        self.is_position_valid(destination)
                        self.is_move_valid(piece, destination)
                        captured_piece = self.get_captured_piece(piece, destination)
                        if captured_piece:
                            legal_moves.append(destination)
                    except Exception:
                        pass
                    try:
                        destination = (new_row + i, new_col - j)
                        self.is_position_valid(destination)
                        self.is_move_valid(piece, destination)
                        captured_piece = self.get_captured_piece(piece, destination)
                        if captured_piece:
                            legal_moves.append(destination)
                    except Exception:
                        pass
        return legal_moves

    def get_all_legal_moves(self, color):
        """
        Returns a list of all legal moves for the given color.

        Parameters:
        - color (str): Color of the player

        Returns: Dictionary of all legal moves for all pieces on the board, grouped by player.
        """
        pieces = self.get_all_pieces(color)
        legal_moves_dict = {}
        # Loop through each piece and get its legal moves
        for piece in pieces:
            legal_moves = self.get_legal_moves(piece)
            legal_moves_dict[piece.position] = legal_moves
        capture_moves = {}
        for pos, moves in legal_moves_dict.items():
            capture_moves[pos] = [move for move in moves if self.get_captured_piece(self.get_piece(pos), move) is not None]
        # If there are capture moves, only return those
        if any(capture_moves.values()):
            return {pos: moves for pos, moves in capture_moves.items() if moves}
        # Return the dictionary of legal moves
        return legal_moves_dict

    def is_move_valid(self, piece, destination):
        """
        Checks if the given move is valid for the given piece.

        Parameters:
        - piece: Piece object
        - destination (Tuple): a tuple of the next postion in the form (row,col),
                       where row and col are integers.

        Returns: True if the move is valid, False otherwise.

        """
        current_position = piece.position
        dy = destination[0] - current_position[0]
        dx = destination[1] - current_position[1]
        # Make sure the destination is not occupied
        if self.get_piece(destination) is not None:
            raise AssertionError("There is already a piece at the destination")
        # Check if the move is a diagonal move
        if abs(dx) != abs(dy):
            raise AssertionError("Move is not diagonal")
        current_position = piece.position
        captured_piece = self.get_captured_piece(piece, destination)
        # If the piece is not a king
        if not piece.is_king:
            if piece.color == Piece.RED and dy > 0:
                raise AssertionError("Piece is not a king and is moving in the wrong direction")
            elif piece.color == Piece.BLACK and dy < 0:
                raise AssertionError("Piece is not a king and is moving in the wrong direction")
            # Check if the move is a capture
            if abs(destination[0] - current_position[0]) == 2 and abs(destination[1] - current_position[1]) == 2:
                # Check if there is a piece to capture
                if captured_piece is None or captured_piece.color == piece.color:
                    raise AssertionError("Invalid move: There is no piece to capture, try again")
            # The move is valid
            return True
        # If the piece is a king
        else:
            # Check if the move is a capture
            if captured_piece!=None:
                # Check if there is a piece to capture
                if captured_piece.color == piece.color:
                    raise AssertionError("There is no piece to capture")
                # The move is valid
                return True
            # The move is not a capture
            return True

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
        current_position = piece.position
        current_piece=self.get_piece(current_position)
        next_piece=self.get_piece(next_position)
        captured_piece = self.get_captured_piece(piece, next_position)
        # Check if there is a piece at the current position
        if current_piece is not None and next_piece is None:
            self.is_move_valid(piece, next_position)
            # Remove piece
            self.remove_piece(current_piece)
            self.remove_piece(captured_piece)
            current_piece.position = next_position
            # Move piece to desitination
            self.Board.board[next_position[0]][next_position[1]] = current_piece
            return self.Board

    def _can_capture_piece(self, piece):
        """
        Checks if the given piece can capture an opposing piece.

        Parameters:
        - piece: Piece object

        Returns: True if the piece can capture, False otherwise.
        """
        legal_moves = self.get_legal_moves(piece)
        # Check if any of the legal moves result in a capture
        for move in legal_moves:
            captured_piece = self.get_captured_piece(piece, move)
            if captured_piece is not None and captured_piece.color != piece.color:
                return True
        # If the piece is a king, check for backward captures as well
        if piece.is_king:
            # Get all the legal moves for the piece in the opposite direction
            move_direction = -1 if piece.color == Piece.BLACK else 1
            for move in [(move_direction, 1), (move_direction, -1)]:
                new_row, new_col = piece.position[0] + move[0], piece.position[1] + move[1]
                destination = (new_row, new_col)
                captured_piece = self.get_captured_piece(piece, destination)
                if captured_piece is not None and captured_piece.color != piece.color:
                    return True
        # If no capture move was found, return False
        return False

    def can_capture_piece(self, player_color):
        """
        Returns True if the given player can capture an opponent's piece, False otherwise.

        Parameters:
        - player_color (str): the color of the player

        Returns: True if the player can capture an opponent's piece, False otherwise.
        """
        pieces = self.get_all_pieces(player_color)
        # Loop through each piece and check if it can capture an opponent's piece
        for piece in pieces:
            if self._can_capture_piece(piece):
                return True        
        # If no piece can capture an opponent's piece, return False
        return False
    

""""
This is a mock implementation of the GUI.

"""
import pygame
from checkers_ed import *

#RGB CODE COLORS
RED = (255, 0, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255) 
GREY = (128, 128, 128) 
GREEN = (0, 255, 0)

#CIRCLE DETAILS
circle_mass = 10
border = 2 

#GAME SETUP
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
FPS = 60

def main():

    # set board size from user input
    print("Welcome to the GUI! How many rows of pieces would you like each side to have?")
    size = input("Enter an integer here: ")
    
    # create your board, players, and game and then play :)
    guib = GUIboard(int(size)) 
    player1 = Player("RED")
    player2 = Player("BLACK")
    new_game = GUIGame(guib, player1, player2)
    new_game.play()    

# An extension of Board that includes functionality to show the board
class GUIboard(Board):
    def __init__(self, n):
        super().__init__(n)
        self.n = n
        self.row = self.dim
        self.col = self.dim
        self.SQUAREDIM = WIDTH // self.row
        self.selected_piece = None
        self.valid_moves = {}
        self.create_guiboard()
    
    def draw_board_squares(self, win):
        win.fill(BLACK)
        for row in range(self.row):
            for col in range(row %2, self.row, 2):
                pygame.draw.rect(win, RED, (row * self.SQUAREDIM, col * self.SQUAREDIM, self.SQUAREDIM, self.SQUAREDIM))

    # fills board with GUIpieces rather than regular Pieces
    def create_guiboard(self):
        for i in range(self.dim):
            row=[]
            for j in range(self.dim):
                if ((i % 2 == 1 and 0 == j % 2 ) or (i % 2 == 0 and 1 == j % 2)) and i <= self.n-1:
                    row.append(GUIpiece(Piece.BLACK, (i,j), self))
                    print(row)
                elif ((i % 2 == 1 and 0 == j % 2 ) or (i % 2 == 0 and 1 == j % 2)) and i > self.dim-self.n-1:
                    row.append(GUIpiece(Piece.RED, (i,j), self))
                    print(row)
                else:
                    row.append(None)
            self.board.append(row)
        
        self.board = self.board[self.dim: ]
        print(self.board)

    def draw_board(self, win):
        self.draw_board_squares(win)
        for row in range(self.row):
            for col in range(self.col):
                piece = self.board[row][col]
                if piece != None:
                    piece.draw(win)

    def highlight_square(self, row, col):
        piece = self.board[row][col]
        if piece:
            piece.highlight(win)
       
        piece.highlight(win)

# An extension of Piece that includes functionality to show a piece
class GUIpiece(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position)
        self.row = self.position[0]
        self.col = self.position[1]
        self.movement_direction = None

        if self.color == "RED":
            self.color = "RED"
            self.pcolor = RED
            self.symbol = 'R'
        else:
            self.color = "BLACK"
            self.pcolor = BLACK
            self.symbol = 'B'

        self.x = 0
        self.y = 0
        self.SQUAREDIM = board.SQUAREDIM
        self.calculate_position()

    def calculate_position(self):
        #to get the middle of the square and align the piece
        self.x = self.SQUAREDIM * self.col + self.SQUAREDIM // 2
        self.y = self.SQUAREDIM * self.row + self.SQUAREDIM // 2

    def draw(self, win):
        radius = self.SQUAREDIM//2 - circle_mass 
        pygame.draw.circle(win, self.pcolor, (self.x, self.y), radius + border)
        pygame.draw.circle(win, WHITE, (self.x, self.y), radius + border, border//2)
        CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (radius + 1, radius + 1))
        if self.is_king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2 - 1 , self.y - CROWN.get_height()//2 - 1))
    
    # used for highlighting a chosen piece
    def highlight(self, win):
        if self.pcolor == WHITE:
            surface = pygame.Surface((self.SQUAREDIM, self.SQUAREDIM))
            surface.set_alpha(100)
            surface.fill((255, 255, 255))
            win.blit(surface, (self.x - self.SQUAREDIM/2, self.y - self.SQUAREDIM/2))
        else:
            surface = pygame.Surface((self.SQUAREDIM, self.SQUAREDIM))
            surface.set_alpha(100)
            surface.fill((0, 0, 0))
            win.blit(surface, (self.x - self.SQUAREDIM/2, self.y - self.SQUAREDIM/2))

    # CHANGE: added move func
    def move(self, row, col):
        self.row = row
        self.col = col
        self.position = (row, col)
        self.calculate_position()

# an extension of Game that replaces the TUI's play() with one that controls the GUI board
class GUIGame(Game):
    def __init__(self, Board, player1, player2):
        """
        Constructor.

        Parameters:
        - board (Object): Board object
        - player1 (Object): First player
        - player2 (Object): Second player
        """
        super().__init__(Board, player1, player2)
        self.board = Board
    
    def play(self):
        """
        Start game and alternate between players until
        game is over.
        """
        run = True
        while run: 
            clock = pygame.time.Clock()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                self.board.draw_board(win)
               
                if event.type == pygame.MOUSEBUTTONDOWN:
                 
                    # Get the position of the mouse
                    mouse_pos = pygame.mouse.get_pos()
                    
                    # Calculate the row and column of the selected square
                    row = mouse_pos[1] // self.board.SQUAREDIM
                    col = mouse_pos[0] // self.board.SQUAREDIM
                    # If choosing a piece to move
                    if self.board.selected_piece is None and self.board.board[row][col] is not None:

                        # set clicked piece to be the selected piece
                        self.board.selected_piece = self.board.board[row][col]
                        self.board.selected_piece_position = (row, col)
                        self.board.highlight_square(row, col)
                        # Get all the legal moves for the piece
                        # This function from the Game Logic portion in the checkers_ed.py file does 
                        #   not accurately find the legal moves
                        legal_moves = self.get_legal_moves(self.board.selected_piece) 
                    # If choosing a location for a previously selected piece to move
                   
                    # Check if we're moving it to a legal position
                    if (row, col) in legal_moves:
                        # Check if this move captures a piece
                        captured_piece = self.get_captured_piece(self.board.selected_piece, (row, col))

                        # Move the piece
                        self.move_piece(self.board.selected_piece, (row, col))
                        self.board.selected_piece.move(row, col)

                        # Check if this move creates a King
                        if row == 0 or row == self.Board.dim - 1:
                            self.board.selected_piece.is_king = True

                        # if captured_piece and self._can_capture_piece(self.board.selected_piece):
                        if captured_piece:
                            print("captured a piece")
                            self.switch_player_turn() # letting capturing player go again

                        # reset selected piece and switch turns
                        self.board.selected_piece = None
                        self.switch_player_turn()
                        print(f"next  players turn: {self.current_player.color}")

                        # theoretically this should tell you who wins once a color is completely captured but it
                        # doesn't work         
                        winner = self.is_game_over()
                        print(f"winner: {winner}")
                        if winner != "RED and BLACK are still playing!":
                            pygame.font.init()
                            font = pygame.font.SysFont('Comic Sans', 32)
                            text = font.render(winner, False, (255, 255, 255))
                            win.blit(text, (0, 0))

            pygame.display.update()
            clock.tick(FPS)
main()



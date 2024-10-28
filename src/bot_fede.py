import random
import checkers_ed

class RandomBot:
    '''
    Bot that picks a random checker move for any move
    '''

    def __init__(self, game, board):
        ''' Constructor

        Args:
            game (Game): Game the bot will play
        '''
        self.game = game
        self.color = game.current_player.color
        self.board = board
        self.moves = game.get_all_legal_moves(self.color)


    def suggest_move(self):
        ''' method that suggests random move

        Returns: None

        '''
        return random.choice(list(self.moves.items()))

class SmarterBot:
    '''
    Smarter bot than RandomBot. It will act as follows:

    - Considers all possible moves one by one
    - If a move will result in an own piece loss, skip it
    - If not, choose that move
    - If all moves result in an own piece loss, choose a random move
    '''
    def __init__(self, game, board):
        ''' Constructor

        Args:
            game (Game): game the bot will play
        '''
        self.game = game
        self.color = game.current_player.color
        self.board = board
        self.moves = game.get_all_legal_moves(self.color)


    def suggest_move(self):
        ''' Suggests a move

        Returns: None

        '''
        if self.game.current_player == self.game.player1:
            self.opponent = game.player2
        else:
            self.opponent = game.player1
        #if all moves result in piece loss, play a random one
        return random.choice(list(self.moves.items()))
        for piece, move in self.moves.items():
            #considers a possible move and tries it
            temp_game = self.game
            temp_game.move_piece(piece, move)
            for opiece, omove in self.opponent.legal_moves.items():
                if not opiece.is_capture_move(board,move):
                    #if move doesn't result in piece loss, return it
                    return piece, move

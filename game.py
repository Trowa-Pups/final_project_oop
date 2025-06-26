#Using my old tic tac toe project and making it cooler and oop style
from win_checker import win_check

class TicTacToe:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.current_player = player_1
        self.other_player = player_2
        self.winner = None
    
    def switch_player(self): #To switch the players in their turns
        self.current_player , self.other_player = self.other_player, self.current_player

    def play(self):
        self.board.display()
        move = self.current_player.get_input(self.board)
        self.board.update_position(move, self.current_player.symbol)

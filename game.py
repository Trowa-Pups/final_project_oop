#Using my old tic tac toe project and making it cooler and oop style
from win_checker import win_check

class TicTacToe:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.current_player = player_1
        self.other_player = player_2
        self.winner = None
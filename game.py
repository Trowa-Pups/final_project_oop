#Using my old tic tac toe project and making it cooler and oop style
from win_checker import WinChecker
from player import Player, OtherPlayer
from board import Board

class TicTacToe:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.current_player = player_1
        self.other_player = player_2
        self.winner = None

    def switch_player(self): #To switch the players in their turns
        self.current_player , self.other_player = self.other_player, self.current_player

    def play(self): #Player turns
        while True:
            win_checker = WinChecker()
            self.board.display_board()
            move = self.current_player.user_inputs(self.board)
            self.board.update_position(move, self.current_player.symbol)

            if win_checker.win_check(self.board, self.current_player.symbol): #To show winner 
                self.board.display_board()
                print(f"The winner is {self.current_player.symbol}!")
                break

            self.board.turn_counter()
            self.switch_player()

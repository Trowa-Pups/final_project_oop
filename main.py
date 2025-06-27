#think of a program/game/app etc, that I think is cool  ✓
#implement the four pillars of OOP in the program 
#Make it cool
#Turned this into main for convenience 
from game import TicTacToe
from player import Player, OtherPlayer
from board import Board

class Main:
    def main():
        board = Board() 
        player_1 = Player("X") #First Player is X
        player_2 = OtherPlayer("O") #Second is O

        game = TicTacToe(board, player_1, player_2)
        game.play() #To launch the game

if __name__ == "__main__":
    Main()
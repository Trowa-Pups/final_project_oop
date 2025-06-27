#think of a program/game/app etc, that I think is cool  ✓
#implement the four pillars of OOP in the program 
#Make it cool
#Turned this into main for convenience 
from game import TicTacToe
from player import Player, OtherPlayer
from board import Board
from colorama import Fore, Style #For cool factor and added Style to reset the color of the text
import time

def main():
    print(Fore.MAGENTA + "♾️" + "\n" + 
    "             Welcome to Infinite TicTacToe!             " + "\n" +
    "                                                   ♾️" + Style.RESET_ALL) #To welcome the user
    time.sleep(2) #To have a smooth transition to the game

    board = Board() 
    player_1 = Player("❌") #First Player is X changed it to an Emoji 
    player_2 = OtherPlayer("⭕") #Second is O changed it to an Emoji 

    game = TicTacToe(board, player_1, player_2)
    game.play() #To launch the game

if __name__ == "__main__":
    while True:
        main()
        replay = str(input(Fore.MAGENTA + "Would you like to play again?(Y/N): ")) #If the user wants to play again
        if replay != "Y":
            print("Thank you for playing Infinite TicTacToe!")
            break
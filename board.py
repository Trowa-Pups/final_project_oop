#This is the board side of the project
from colorama import Fore
class Board():
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]  
        
        self.turns = [0] * 9 #Changed it to this so that its not the same as the def turn_counter

    def display_board(self): #Added more spaces to make it more big
        print(self.board[0] + "  |  " + self.board[1] + "  |  " + self.board[2] + "\n" +"\n"
          + "--------------" + "\n" + "\n"
          + self.board[3] + "  |  " + self.board[4] + "  |  " + self.board[5] + "\n" + "\n"
          + "--------------" + "\n" + "\n"
          + self.board[6] + "  |  " + self.board[7] + "  |  " + self.board[8])
    
    def update_position(self, position, current_player): #This part is where it counts what lifespan of the symbol
        self.board[position] = current_player
        self.turns[position] = 6 #Also realized i input self.board on this not self.turns,  it supposed to be the symbol lifespan

    def turn_counter(self):
        for i in range(9):
            if self.turns[i] > 0:
                self.turns[i] -= 1 
                if self.turns[i] == 0:
                    self.board[i] = "-"

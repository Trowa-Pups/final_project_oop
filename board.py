#This is the board side of the project
class Board():
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]  
        
        self.turns = [0] * 9

    def display_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "\n"
          + "---------" + "\n"
          + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "\n"
          + "---------" + "\n"
          + self.board[6] + " | " + self.board[7] + " | " + self.board[8])
    
    def update_position(self, position, current_player): #This part is where it counts what lifespan of the symbol
        self.board[position] = current_player
        self.turns[position] = 6

    def turn_counter(self):
        for i in range(9):
            if self.turns > 0:
                self.turns -= 1
                if self.turns == 0:
                    self.board = "-"



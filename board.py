#This is the board side of the project
class Board():
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]  
        
        self.turn_coutner = [0] * 9
        

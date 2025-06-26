#This file checks the board if a specific symbol has a win condition
class WinChecker:
    def win_check(self, board, symbol):
        win_conditions = [[board[0], board[1], board[2]] #Horizontal
                          [board[3], board[4], board[5]]
                          [board[6], board[7], board[8]]
                          [board[0], board[3], board[6]] #Vertical
                          [board[1], board[4], board[7]]
                          [board[2], board[5], board[8]]
                          [board[0], board[4], board[8]] #Diagonal
                          [board[2], board[4], board[6]]
                          ]
        
        for condition in win conditions: #checks if one of the conditions are met
            if all(cell == symbol for cell in condition):
                return True
            
        return False
        

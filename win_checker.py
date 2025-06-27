#This file checks the board if a specific symbol has a win condition
class WinChecker:
    def win_check(self, board, symbol):
        win_conditions = [[board.board[0], board.board[1], board.board[2]], #Horizontal
                          [board.board[3], board.board[4], board.board[5]],
                          [board.board[6], board.board[7], board.board[8]],
                          [board.board[0], board.board[3], board.board[6]], #Vertical
                          [board.board[1], board.board[4], board.board[7]],
                          [board.board[2], board.board[5], board.board[8]],
                          [board.board[0], board.board[4], board.board[8]], #Diagonal
                          [board.board[2], board.board[4], board.board[6]],
                          ]
        
        for condition in win_conditions: #checks if one of the conditions are met
            if all(cell == symbol for cell in condition):
                return True
            
        return False
        

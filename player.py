#This is where the player and input part of the project is
class Player:
    def __init__(self, symbol):  #Making this so that it can be both X and O
        self.symbol = symbol
    
    def user_inputs(self, board): #Trying to copy the project so i put self and board just in case
        while True:
            try:
                user_input = int(input("Enter a number between 1 to 9!")) - 1 #Putting - 1 here so i dont need to make it [user_input - 1]

                if 0 <= user_input <= 8 and board.board[user_input] == "-":
                    return user_input #To store the player's input value
            
                else:
                    print("Invalid Move! Please try again")

            except ValueError:
                print("Invalid Value! Please input 1 to 9")

class OtherPlayer(Player): #For Polymorphism 
    def get_input(self, board):
        return super().user_input(board)
        
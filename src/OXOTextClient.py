from GameClient import *

class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-8):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self):
        print("_________________________") #25 Underscores to create the first horizontal bisecting line
        print()
        count = 0
        for b in range(3):
            print("|  ", end="")
            for m in range(3):  #creating 3 bisecting vertical lines
                print("  " + self.board[count]+"  |  ", end="")
                count = count + 1

            print()
            print("_________________________") #25 Underscores to create the second horizontal bisecting line
            print()

        pass
    
    def handle_message(self,msg):
        message = msg.strip().split(",")

        if (message[0].lower() == "new game"):
            self.display_board()
            self.shape = message[1]
            print("The game has started, your character is " + message[1])

        elif (message[0].lower() == "your move"):
            self.display_board()
            self.yourMove = self.input_move()
            self.send_message(self.yourMove)

        elif (message[0].lower() == "opponets move"):
            print("opponent's move")
            # print(message[0])

        elif (message[0].lower() == "valid move"):
            self.shape = message[1]
            self.Position = message[2]
            self.Position = int(self.Position)
            self.board[self.Position] = self.shape
            self.display_board()
            return "valid move"

        elif (message[0].lower() == "invalid move"):
            print(message[0])

        elif (message[0].lower() == "game over"):
            print("Final game Board.")
            self.display_board()
            if (message[1] == "T"):
                print("It's a tie")
            else:
                print("Game over, the winner is {}".format(message[1].upper()))
            return "game over"

        elif (message[0].lower() == "play again"):
            self.response = self.input_play_again()
            if self.response == 'y':
                self.clear_board()
            self.send_message(self.response)

        elif (message[0].lower() == "exit game"):
            print("Nice playing with you.")

        pass
    
    def play_again(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
def main():
    otc = OXOTextClient()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_again()
    input('Press click to exit.')
        
main()
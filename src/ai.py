class AI:
    def solve(self, board):
        while not board.win():
            print("Computer's move")
            # AI's logic goes here
            break
        return False
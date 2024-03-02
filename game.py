from player import Player
from ai import AI
from graph import Graph


class Game:
    def __init__(self):
        self.current_player = None

    def start_game(self, file_name):
        print("""---------------------------------
              Masyu solver
              
              Please select an option:
                1. Play
                2. Let the computer solve it
                3. Exit
              """)
        
        graph = Graph(file_name)
        option = input("Option: ")
        if option == "1":
            self.current_player = "human"
        elif option == "2":
            self.current_player = "ai"
        elif option == "3":
            exit(0)
        else:
            print("Invalid option. Please try again.")
            self.start()
        return self.current_player, graph
            
    def game_flow(self):
        current_player, board = self.start()
        
        while not board.win():
            if current_player == "human":
                player = Player()
                player.make_move(board)
            elif current_player == "ai":
                ai = AI()
                ai.make_move(board)
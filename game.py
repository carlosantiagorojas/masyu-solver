from player import Player
from ai import AI
from graph import Graph


class Game:
    def __init__(self):
        self.current_player = None

    def menu(self):
        print("------------------------------")
        print("Masyu solver")
        print()
        print("Please select an option:")
        print("1. Play")
        print("2. Let the AI solve it")
        print("3. Exit")
        print("------------------------------")

        while True:
            try:
                option = int(input("Option: ").strip())
                if 1 <= option <= 3:
                    if option == 1:
                        self.current_player = "human"
                    elif option == 2:
                        self.current_player = "ai"
                    elif option == 3:
                        break
                    break
                else:
                    print("\nInvalid option. Please try again")
            except ValueError:
                print("\nERROR: Please type in the correct format")
        return self.current_player

    def game_flow(self, file_name):
        board = self.create_board(file_name)
        player = Player()
        ai = AI()
        
        while True:
            current_player = self.menu()
            if current_player == None:
                break
            
            while not board.win():
                if current_player == "human":
                    print("\n\n==============================")
                    print("Player game mode")
                    print("==============================\n")
                    print(board)
                    if not player.make_move(board):
                        break
                        
                elif current_player == "ai":
                    print("\n\n==============================")
                    print("AI solver")
                    print("==============================\n")
                    print(board)
                    ai.solve(board)
                    if not player.solve(board):
                        print("AI could not solve the puzzle")
                        break
    
    def create_board(self, file_name):
        return Graph(file_name)
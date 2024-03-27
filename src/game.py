from src.ai import AI
from src.graph import Graph
from src.player import Player


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
              return self.current_player
            else:
              print("\nInvalid option. Please try again")
              break  # Exit on first invalid input
          except ValueError:
            print("\nERROR: Please type in the correct format")

    def game_flow(self, file_name):
        player = Player()
        ai = AI()
        while True:
            board = Graph(file_name)
            current_player = self.menu()

            if current_player == None:
                break
            elif current_player == "human":
                print("\n\n==============================")
                print("Player game mode")
                print("==============================\n")
                # print(board)
                if not player.play(board):
                    break
            else:
                print("\n\n==============================")
                print("AI game mode")
                print("==============================\n")
                # print(board)
                if not ai.solve(board):
                    print("AI could not solve the puzzle")
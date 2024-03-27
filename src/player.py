import tkinter as tk
from src.gui import GUI


class Player:
    def play(self, board):
        try:
            root = tk.Tk()
            # This line brings the window to the front
            root.attributes('-topmost', True)
            app = GUI(root, board)
            root.mainloop()
            return True
        except Exception as e:
            print("\nERROR:", e)
            return False


    # def make_move(self, board):
    #     board_size = board.size
    #     while True:
    #         try:
    #             line_start = input(
    #             "\nType the number of the row and column separated by a ','\nwhere you want the line to start or 'exit' to exit menu: ")
    #             if line_start.lower() == "exit":
    #                 return False
    #             else:
    #                 try:
    #                     s_row, s_column = map(int, line_start.strip().split(','))
    #                 except ValueError:
    #                     raise ValueError("Invalid input. Please enter two numbers separated by a comma")
    #                 if s_column > board_size or s_row > board_size:
    #                     raise ValueError("Row or column exceeds board dimensions. Please try again")
    #             # print(s_column, s_row)

    #             line_end = input(
    #                 "\nType the number of the row and column separated by a ','\nwhere you want the line to end or 'exit' to exit menu: ")
    #             if line_end.lower() == "exit":
    #                 return False
    #             else:
    #                 try:
    #                     e_row, e_column = map(int, line_end.strip().split(','))
    #                 except ValueError:
    #                     raise ValueError("Invalid input. Please enter two numbers separated by a comma")
    #                 if e_column > board_size or e_row > board_size:
    #                     raise ValueError("Row or column exceeds board dimensions. Please try again")
    #             # print(e_column, e_row)
                
    #             if s_row == e_row and s_column == e_column:
    #                 raise ValueError("The start and end points are the same. Please try again")
                
    #             # Add the edge to the graph
    #             board.add_edge(s_row - 1, s_column - 1, e_row - 1, e_column - 1)
                
    #             return True
    #         except ValueError as e:
    #             print("\nERROR:", e)
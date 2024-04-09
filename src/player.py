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
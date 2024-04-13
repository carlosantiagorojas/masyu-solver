class colors:
    """Class to store the colors of the game
    """
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 45, 0)
        self.GREEN = (0, 255, 0)

        self.flag = False

    def change_dark_mode(self):
        """Changes the colors of the game to dark mode or light mode
        """
        if not self.flag:
            self.BLACK = (0, 0, 0)
            self.WHITE = (70, 70, 70)
            self.flag = True
        else:
            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.flag = False
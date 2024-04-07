import tkinter as tk


class GUI:
    def __init__(self, master, board):
        self.master = master  # The parent widget
        self.graph = board  # The graph data
        self.clicked_buttons = []  # List to store the clicked cells
        self.lines = {}  # Dictionary to store the lines drawn between cells
        self.canvas = tk.Canvas(master, width=500, height=500)  # The canvas widget
        self.canvas.pack()  # Display the canvas

        # Create the cells on the canvas
        for i in range(6):
            for j in range(6):
                node = self.graph.adjacency_matrix[i][j]
                if node.color == 1:
                    # Create a white cell
                    oval = self.canvas.create_oval(j*83+10, i*83+10, j*83+73, i*83+73, fill='white')
                elif node.color == 2:
                    # Create a black cell
                    oval = self.canvas.create_oval(j*83+10, i*83+10, j*83+73, i*83+73, fill='black')
                else:
                    # Create an empty cell
                    oval = self.canvas.create_oval(j*83+30, i*83+30, j*83+53, i*83+53, fill='black')
                # Bind the click event to the cell
                self.canvas.tag_bind(oval, "<Button-1>", lambda e, x=i, y=j: self.on_oval_click(x, y))

    def on_oval_click(self, x, y):
        # Handle the click event on a cell, it accesses the cell's coordinates (x, y)
        if not self.clicked_buttons or self.clicked_buttons[-1] != (x, y):
            self.clicked_buttons.append((x, y))
        # If two cells have been clicked, check if they are adjacent
        if len(self.clicked_buttons) == 2:
            points = tuple(sorted(self.clicked_buttons))
            if points in self.lines:
                # If a line already exists between the cells, remove it
                self.canvas.delete(self.lines[points])
                del self.lines[points]
                print(f"Removed line between {points[0]} and {points[1]}")
                s_x, s_y = points[0]
                e_x, e_y = points[1]
                self.graph.remove_edge(s_x, s_y, e_x, e_y)
                print(self.graph.check_win())
            # Check if the cells are adjacent to each other
            elif (
                (abs(self.clicked_buttons[0][0] - self.clicked_buttons[1][0]) == 1 and 
                self.clicked_buttons[0][1] == self.clicked_buttons[1][1]) 
                or 
                (abs(self.clicked_buttons[0][1] - self.clicked_buttons[1][1]) == 1 and 
                self.clicked_buttons[0][0] == self.clicked_buttons[1][0])
            ):
                # If the cells are adjacent, draw a line between them
                self.draw_line(*points)
                print(f"Drawn line between {points[0]} and {points[1]}")
                s_x, s_y = points[0]
                e_x, e_y = points[1]
                self.graph.add_edge(s_x, s_y, e_x, e_y)
                print(self.graph.check_win())
            # Clear the clicked cells
            self.clicked_buttons = []

    def draw_line(self, point1, point2):
        # Draw a line between two cells
        line_id = self.canvas.create_line(
            point1[1]*83+41.5, 
            point1[0]*83+41.5, 
            point2[1]*83+41.5, 
            point2[0]*83+41.5, 
            width=2
        )
        self.lines[(point1, point2)] = line_id  # Store the line
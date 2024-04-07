from src.node import Node


class Graph:
    def __init__(self, file_name) -> None:
        self.all_nodes = []
        self.adjacency_matrix = self.create_adjacency_matrix(file_name)
        self.size = len(self.adjacency_matrix)

    def create_adjacency_matrix(self, file_name):
        with open(file_name, 'r') as file:
            # Read the first line to get the dimensions of the matrix    
            dimensions = int(file.readline().strip())
            
            adjacency_matrix = [[None for _ in range(
                dimensions)] for _ in range(dimensions)]
            
            # Read the rest of the file to fill the matrix
            for line in file:
                row, col, color = map(int, line.strip().split(','))
                # print(adjacency_matrix[row - 1][col - 1])
                adjacency_matrix[row - 1][col - 1] = Node(color, row - 1, col - 1)
                # print(adjacency_matrix[row - 1][col - 1])
                self.all_nodes.append(adjacency_matrix[row - 1][col - 1])
                # print(self.all_nodes)
        
        # Fill the matrix with the spaces                
        for i in range(dimensions):
            for j in range(dimensions):
                if adjacency_matrix[i][j] is None:
                    adjacency_matrix[i][j] = Node(None, i, j)
                
        return adjacency_matrix
            
    def add_edge(self, s_x: int, s_y: int, e_x: int, e_y: int) -> None:
        """
        Add an edge between two nodes
        """
        # print(f"Adding edge between ({s_x}, {s_y}) and ({e_x}, {e_y})")
        self.adjacency_matrix[s_x][s_y].weight += 1
        self.adjacency_matrix[e_x][e_y].weight += 1
        # print(f"Weight of ({s_x}, {s_y}): {self.adjacency_matrix[s_x][s_y].weight}")
        # print(f"Weight of ({e_x}, {e_y}): {self.adjacency_matrix[e_x][e_y].weight}")
        # Implement logic
        pass    
    
    def remove_edge(self, s_x: int, s_y: int, e_x: int, e_y: int) -> None:
        """
        Add an edge between two nodes
        """
        print("enter here")
        # print(f"Adding edge between ({s_x}, {s_y}) and ({e_x}, {e_y})")
        self.adjacency_matrix[s_x][s_y].weight -= 1
        self.adjacency_matrix[e_x][e_y].weight -= 1
        # print(f"Weight of ({s_x}, {s_y}): {self.adjacency_matrix[s_x][s_y].weight}")
        # print(f"Weight of ({e_x}, {e_y}): {self.adjacency_matrix[e_x][e_y].weight}")
        # Implement logic
        pass  
    
    def check_win(self) -> bool:
        """
        Check if the game is over, this is when the graph is cyclic
        """
        # Implement logic
        # print(self.all_nodes[0].weight)
        if self.check_valid_black(0,0):
            return True
        return False
    
    def dfs(self, x, y) -> bool:
        """
        Perform a depth-first search on the graph
        """
        # Implement logic
        return False
    
    def check_valid_black(self, x, y) -> bool:
        """
        Check if the black node is valid or not
        """
        valid = False
        if self.adjacency_matrix[x][y].valid_connections():
            if self.check_adyacent_black(x, y):
                valid = True

        return valid
    
    def check_valid_white(self, x, y) -> bool:
        """check if the black node is valid or not
        """
        valid = False
        if self.adjacency_matrix[x][y].valid_connections():
            if self.check_adyacent_white(x, y):
                valid = True
        return valid
         
    def check_adyacent_black(self, x, y) -> bool:
        """return in what positions are the two adyacent nodes that are connected to the node
        Args:
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            bool
        """
        pos_adyacent = []
        
        node = self.adjacency_matrix[x - 2][y]
        # check left
        if ((x - 2) >= 0):
            print("entre left")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                and self.adjacency_matrix[x - 2][y].valid_connections()):
                pos_adyacent.append(1)

        # check up
        if ((y - 2) >= 0):
            print("entre up")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                and self.adjacency_matrix[x][y - 2].valid_connections()):
                pos_adyacent.append(2)

        # check down
        if ((self.size - y) >= 2):
            print("entre down")
            if (self.adjacency_matrix[x][y + 1].valid_connections()
                and self.adjacency_matrix[x][y + 2].valid_connections()
                and not 2 in pos_adyacent):
                pos_adyacent.append(3)

        # check right
        if ((self.size - x) >= 2):
            print("entre right")
            if (self.adjacency_matrix[x + 1][y].valid_connections()
                and self.adjacency_matrix[x + 2][y].valid_connections() 
                and not 1 in pos_adyacent):
                    pos_adyacent.append(4)
                
        if len(pos_adyacent) == 2:
                return True
        return False
    
    def check_adyacent_white(self, x, y):
        row_direction = False
        column_direction = False
        turn_col_left = False
        turn_col_right = False
        turn_row_left = False
        turn_row_right = False
        valid = False
        
        # check an adyacent connection
        # check left and right
        if (self.adjacency_matrix[x - 1][y].valid_connections()
            and self.adjacency_matrix[x + 1][y].valid_connections()):
                row_direction = True
        # check up and down
        if (self.adjacency_matrix[x][y - 1].valid_connections()
            and self.adjacency_matrix[x][y + 1].valid_connections()):
                column_direction = True
        
        # check turn   
        if row_direction or column_direction:
            # check connection turn to a column or row
            # check left
            if (self.adjacency_matrix[x - 1][y - 1].valid_connections()
               or self.adjacency_matrix[x - 1][y + 1].valid_connections()):
                turn_col_left = True
                turn_row_left = True
            # check right
            elif (self.adjacency_matrix[x + 1][y - 1].valid_connections()
               or self.adjacency_matrix[x + 1][y + 1].valid_connections()):
                turn_col_right = True
                turn_row_right = True

        # check if there is two continuous connections
        if turn_col_left:
            if not self.adjacency_matrix[x - 2][y].valid_connections():
                valid = True
        if turn_col_right:
            if not self.adjacency_matrix[x + 2][y].valid_connections():
                valid = True
        if turn_row_left:
            if not self.adjacency_matrix[x][y - 2].valid_connections():
                valid = True
        if turn_row_right:
            if not self.adjacency_matrix[x][y + 2].valid_connections():
                valid = True
        
        return valid
        
    # def __str__(self) -> str:
    #     matrix_str = "-" * 37 + "\n"
    #     for i in range(self.size):
    #         matrix_str += "|"
    #         for j in range(self.size):
    #             node = self.adjacency_matrix[i][j]
    #             if node is not None:
    #                 cell_str = ""
    #                 if node.color == 1:
    #                     # Use a Unicode character to represent a black circle
    #                     cell_str = " \u25CF "
    #                 elif node.color == 2:
    #                     # Use a Unicode character to represent a white circle
    #                     cell_str = " \u25CB "
    #                 # Check if the node weight is greater than 0
    #                 if node.weight > 0:
    #                     # Use a Unicode character to represent a line
    #                     if node.up or node.down:
    #                         cell_str = " \u2502 "  # Vertical line
    #                     if node.left or node.right:
    #                         cell_str = " \u2500 "  # Horizontal line
    #                 matrix_str += cell_str.center(5) + "|"
    #             else:
    #                 matrix_str += "".center(5) + "|"
    #         matrix_str += "\n" + "-" * 37 + "\n"
    # return matrix_str
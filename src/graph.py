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
        self.adjacency_matrix[s_x][s_y].weight += 1
        self.adjacency_matrix[e_x][e_y].weight += 1  
    
    
    def remove_edge(self, s_x: int, s_y: int, e_x: int, e_y: int) -> None:
        """
        Add an edge between two nodes
        """
        self.adjacency_matrix[s_x][s_y].weight -= 1
        self.adjacency_matrix[e_x][e_y].weight -= 1

    
    def check_win(self) -> bool:
        """
        Check if the game is over, this is when the graph is cyclic
        """
        # Implement logic
        print(self.all_nodes[7].weight)
        print(self.check_valid_white(2,3))
        return self.check_valid_white(2,3)
    
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
        print("fasfda",self.adjacency_matrix[x][y].weight)
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
        
        # check left
        if ((y - 2) >= 0):
            print("entre left")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                and self.adjacency_matrix[x - 2][y].valid_connections()):
                pos_adyacent.append(1)

        # check up
        if ((x - 2) >= 0):
            print("entre up")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                and self.adjacency_matrix[x][y - 2].valid_connections()):
                pos_adyacent.append(2)

        # check down
        if ((self.size - x + 1) >= 2):
            print("entre down")
            if (self.adjacency_matrix[x][y + 1].valid_connections()
                and self.adjacency_matrix[x][y + 2].valid_connections()
                and not 2 in pos_adyacent):
                pos_adyacent.append(3)

        # check right
        if ((self.size - y + 1) >= 2):
            print("entre right")
            if (self.adjacency_matrix[x + 1][y].valid_connections()
                and self.adjacency_matrix[x + 2][y].valid_connections() 
                and not 1 in pos_adyacent):
                    pos_adyacent.append(4)
                
        if len(pos_adyacent) == 2:
                return True
        return False
    
    def check_adyacent_white(self, x, y):
        print("entre metodo")
        row_direction = False
        column_direction = False
        # turn_col_left = False
        # turn_col_right = False
        # turn_row_left = False
        # turn_row_right = False
        # valid = False
        first_row = False
        last_row = False
        first_col = False
        last_col = False
        # check an adyacent connection
        print("pato")
        # if is on the first row
        # check left and right
        if ((x - 1) < 0):
            print("auida1")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                and self.adjacency_matrix[x][y + 1].valid_connections()):
                first_row = True
                
        # if is on the last row
        # check left and right
        elif ((self.size - x + 1) == 0):
            print("auida2")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                and self.adjacency_matrix[x][y + 1].valid_connections()):
                last_row = True
        
        # if is on the first column
        # check up and down
        elif ((y - 1) < 0):
            print("auida3")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                and self.adjacency_matrix[x - 1][y].valid_connections()):
                first_col = True
        
        # if is on the last column
        # check up and down
        elif ((self.size - y + 1) == 0): 
            print("auida4")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                and self.adjacency_matrix[x - 1][y].valid_connections()):
                last_col = True
        
        else:
            print("auida")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                and self.adjacency_matrix[x + 1][y].valid_connections()):
                print("entre aquib")
                column_direction = True
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                and self.adjacency_matrix[x][y + 1].valid_connections()):
                print("entre aquia")
                row_direction = True
        
        # check turns
        
        # if is on the first row
        if first_row:
            if (self.adjacency_matrix[x + 1][y - 1].valid_connections()
                or self.adjacency_matrix[x + 1][y + 1].valid_connections()):
                return True
        # if is on the last row
        if last_row:
            if (self.adjacency_matrix[x - 1][y - 1].valid_connections()
                and self.adjacency_matrix[x - 1][y + 1].valid_connections()):
                return True
        # if is on the first column
        if first_col:
            if (self.adjacency_matrix[x - 1][y + 1].valid_connections()
                or self.adjacency_matrix[x + 1][y + 1].valid_connections()):
                return True
        # if is on the last column
        if last_col: 
            if (self.adjacency_matrix[x - 1][y - 1].valid_connections()
                and self.adjacency_matrix[x + 1][y - 1].valid_connections()):
                return True
        
        # check turn   
        if row_direction or column_direction:
            print("entre aqui2")
            # check connection turn to a column or row
            # check left
            if (self.adjacency_matrix[x - 1][y - 1].valid_connections()
                   or self.adjacency_matrix[x + 1][y - 1].valid_connections()
                   or self.adjacency_matrix[x - 1][y + 1].valid_connections()
                   or self.adjacency_matrix[x + 1][y + 1].valid_connections()):
                print("entre aqui3")
                return True

        # # check if there is two continuous connections
        # if turn_col_left:
        #     if not self.adjacency_matrix[x - 2][y].valid_connections():
        #         valid = True
        # if turn_col_right:
        #     if not self.adjacency_matrix[x + 2][y].valid_connections():
        #         valid = True
        # if turn_row_left:
        #     if not self.adjacency_matrix[x][y - 2].valid_connections():
        #         valid = True
        # if turn_row_right:
        #     if not self.adjacency_matrix[x][y + 2].valid_connections():
        #         valid = True
        
        return False
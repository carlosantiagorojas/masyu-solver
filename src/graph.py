from node import Node


class Graph:
    def __init__(self, file_name) -> None:
        self.adjacency_matrix = self.create_adjacency_matrix(file_name)
        self.size = len(self.adjacency_matrix)
        self.connected_nodes = []

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
                adjacency_matrix[row - 1][col -
                                          1] = Node(color, row - 1, col - 1)
                # print(adjacency_matrix[row - 1][col - 1])

        # Fill the matrix with the spaces
        for i in range(dimensions):
            for j in range(dimensions):
                if adjacency_matrix[i][j] is None:
                    adjacency_matrix[i][j] = Node(None, i, j)

        return adjacency_matrix

    def create_circle_data(self, file_name):
        circle_data = {}
        with open(file_name, 'r') as file:
            # Skip the first line (dimensions)
            next(file)

            # Read the rest of the file to fill the dictionary
            for line in file:
                row, col, color = map(int, line.strip().split(','))
                circle_data[(row, col)] = color
        return circle_data

    def add_edge(self, s_x: int, s_y: int, e_x: int, e_y: int) -> None:
        """
        Add an edge between two nodes
        """
        start_node = self.adjacency_matrix[s_x][s_y]
        end_node = self.adjacency_matrix[e_x][e_y]
        print("adding")
        print(start_node, end_node)

        # add weight
        end_node.weight += 1
        start_node.weight += 1

        # add node in the start node adjacent list
        start_node.add_adjacent_node(end_node)
        end_node.add_adjacent_node(start_node)

        # print()
        # print("Start node...")
        # print(f"Adjacent nodes of {start_node}:")
        # for node in start_node.adjacency_list:
        #     print(node, end= " ")
        # print()

        # print("End node...")
        # print(f"Adjacent nodes of {end_node}:")
        # for node in end_node.adjacency_list:
        #     print(node, end=" ")
        # print()

    def remove_edge(self, s_x: int, s_y: int, e_x: int, e_y: int) -> None:
        """
        Remove an edge between two nodes
        """
        start_node = self.adjacency_matrix[s_x][s_y]
        end_node = self.adjacency_matrix[e_x][e_y]
        print("removing")
        print(start_node, end_node)
        # decrease weight
        end_node.weight -= 1
        start_node.weight -= 1

        # remove node from the start node adjacent list
        start_node.remove_adjacent_node(end_node)
        end_node.remove_adjacent_node(start_node)

    def get_connected_nodes(self):
        for row in self.adjacency_matrix:
            for node in row:
                if node.list_size() > 0 and node not in self.connected_nodes:
                    self.connected_nodes.append(node)

    def remove_all_connected_nodes(self):
        self.connected_nodes.clear()

    def all_valid_connections(self):
        for row in self.adjacency_matrix:
            for node in row:
                if node.weight > 2:
                    return False
        return True

    def check_win(self) -> bool:
        """
        Check if the game is over, this is when the graph is cyclic
        """
        self.remove_all_connected_nodes()
        self.get_connected_nodes()
        self.print_connected_nodes()
        return self.is_cyclic()

    class InvalidNodeException(Exception):
        pass
    
    def dfs(self, current_node, visited, parent_node):
        print(f"Visiting node: {current_node}")
        visited.append(current_node)
    
        # Validate the node based on its color
        if current_node.color == 1:  # White
            if not self.check_valid_white(current_node):
                print("Node is white, checking validity...")
                print("Node is not valid, raising InvalidNodeException")
                raise Graph.InvalidNodeException
            print("Node is valid")
    
        elif current_node.color == 2:  # Black
            if not self.check_valid_black(current_node):
                print("Node is white, checking validity...")
                print("Node is not valid, raising InvalidNodeException")
                raise Graph.InvalidNodeException
            print("Node is valid")
    
        for adjacent_node in current_node.adjacency_list:
            if adjacent_node not in visited:
                # print(f"Node {adjacent_node} is not visited, visiting it...")
                self.dfs(adjacent_node, visited, current_node)
            elif adjacent_node != parent_node:
                print("Found a cycle, returning True")
                return True
    
        # print("Finished visiting all adjacent nodes, returning False")
        return False
    
    def is_cyclic(self):
        if not self.all_valid_connections():
            return False
    
        self.get_connected_nodes()
    
        node = self.connected_nodes[0]
        visited = []  # Clear the visited list for each new starting node

        try:
            if self.dfs(node, visited, None) is True:
                print("Found a cycle, graph is cyclic")
                return True
        except Graph.InvalidNodeException:
            print("Invalid node found, stopping DFS")
            return False

    def check_valid_black(self, node: Node) -> bool:
        """
        Check if the black node is valid or not
        """
        valid = False
        if self.check_adyacent_black(node.x, node.y):
            valid = True

        return valid

    def check_valid_white(self, node: Node) -> bool:
        """check if the black node is valid or not
        """
        valid = False
        # print("fasfda", self.adjacency_matrix[x][y].weight)
        if self.check_adyacent_white(node.x, node.y):
            valid = True
        return valid

    def check_adyacent_black(self, x, y) -> bool:
        """return in what positions are the two adyacent nodes that are connected to the node
        """
        pos_adyacent = []

        # check down
        if (0 <= (x + 1) <= (self.size - 2)):
            # print("check down")
            if (self.adjacency_matrix[x + 1][y].valid_connections()
                    and self.adjacency_matrix[x + 2][y].valid_connections()):
                pos_adyacent.append(1)

        # check left
        if (3 <= (y + 1) <= self.size):
            # print("check left")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                    and self.adjacency_matrix[x][y - 2].valid_connections()):
                pos_adyacent.append(2)

        # check right
        if (0 <= (y + 1) <= (self.size - 3)):
            # print("check right")
            if (self.adjacency_matrix[x][y + 1].valid_connections()
                and self.adjacency_matrix[x][y + 2].valid_connections()
                    and not 2 in pos_adyacent):
                pos_adyacent.append(3)

        # check up
        if (3 <= (x + 1) <= self.size):
            # print("check up")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                and self.adjacency_matrix[x - 2][y].valid_connections()
                    and not 1 in pos_adyacent):
                pos_adyacent.append(4)

        if len(pos_adyacent) == 2:
            return True
        return False

    def check_adyacent_white(self, x, y):
        in_column = False
        in_row = False
        first_row = False
        last_row = False
        first_col = False
        last_col = False
        # check an adyacent connection

        # if is on the first row
        # check left and right
        if (x == 0):
            # print("auida1")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                    and self.adjacency_matrix[x][y + 1].valid_connections()):
                first_row = True

        # if is on the last row
        # check left and right
        elif ((x + 1) == self.size):
            # print("auida2")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                    and self.adjacency_matrix[x][y + 1].valid_connections()):
                last_row = True

        # if is on the first column
        # check up and down
        elif (y == 0):
            # print("auida3")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                    and self.adjacency_matrix[x - 1][y].valid_connections()):
                first_col = True

        # if is on the last column
        # check up and down
        elif ((y + 1) == self.size):
            # print("auida4")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                    and self.adjacency_matrix[x - 1][y].valid_connections()):
                last_col = True

        else:
            # print("auida")
            if (self.adjacency_matrix[x - 1][y].valid_connections()
                    and self.adjacency_matrix[x + 1][y].valid_connections()):
                # print("entre aquib")
                in_column = True

            elif (self.adjacency_matrix[x][y - 1].valid_connections()
                    and self.adjacency_matrix[x][y + 1].valid_connections()):
                # print("entre aquia")
                in_row = True

        # check turns

        # if is on the first row
        if first_row:
            if ((self.adjacency_matrix[x + 1][y - 1].valid_connections()
                and self.adjacency_matrix[x + 1][y - 1] in self.adjacency_matrix[x][y - 1].adjacency_list)
                or (self.adjacency_matrix[x + 1][y + 1].valid_connections()
                and self.adjacency_matrix[x + 1][y + 1] in self.adjacency_matrix[x][y + 1].adjacency_list)):                    
                return True
        # if is on the last row
        elif last_row:
            if ((self.adjacency_matrix[x - 1][y - 1].valid_connections()
                and self.adjacency_matrix[x - 1][y - 1] in self.adjacency_matrix[x][y - 1].adjacency_list)
                or (self.adjacency_matrix[x - 1][y + 1].valid_connections()
                and self.adjacency_matrix[x - 1][y + 1] in self.adjacency_matrix[x][y + 1].adjacency_list)):
                return True
        # if is on the first column
        elif first_col:
            if ((self.adjacency_matrix[x - 1][y + 1].valid_connections()
                and self.adjacency_matrix[x - 1][y + 1] in self.adjacency_matrix[x - 1][y].adjacency_list)
                or (self.adjacency_matrix[x + 1][y + 1].valid_connections()
                and self.adjacency_matrix[x + 1][y + 1] in self.adjacency_matrix[x + 1][y].adjacency_list)):
                return True
        # if is on the last column
        elif last_col:
            if ((self.adjacency_matrix[x - 1][y - 1].valid_connections()
                and self.adjacency_matrix[x - 1][y - 1] in self.adjacency_matrix[x - 1][y].adjacency_list)
                or (self.adjacency_matrix[x + 1][y - 1].valid_connections()
                and self.adjacency_matrix[x + 1][y - 1] in self.adjacency_matrix[x + 1][y].adjacency_list)):
                return True

        # check turn
        elif in_column:
            # check connection turn to a column or row
            # check left
            # print(
            #     (self.adjacency_matrix[x - 1][y + 1],
            #     self.adjacency_matrix[x - 1][y + 1] in self.adjacency_matrix[x][y].adjacency_list))
            
            # x - 1 
            if self.adjacency_matrix[x - 1][y - 1] in self.adjacency_matrix[x - 1][y].adjacency_list:
                return True
            elif self.adjacency_matrix[x - 1][y + 1] in self.adjacency_matrix[x - 1][y].adjacency_list:
                return True
            
            # x + 1
            elif self.adjacency_matrix[x + 1][y - 1] in self.adjacency_matrix[x + 1][y].adjacency_list:
                return True
            elif self.adjacency_matrix[x + 1][y + 1] in self.adjacency_matrix[x + 1][y].adjacency_list:
                return True
            
            # if ((self.adjacency_matrix[x - 1][y - 1].valid_connections()
            #     and self.adjacency_matrix[x - 1][y - 1] in self.adjacency_matrix[x][y].adjacency_list)
            #     or (self.adjacency_matrix[x + 1][y - 1].valid_connections()
            #     and self.adjacency_matrix[x + 1][y - 1] in self.adjacency_matrix[x][y].adjacency_list)
            #     or (self.adjacency_matrix[x - 1][y + 1].valid_connections()
            #     and self.adjacency_matrix[x - 1][y + 1] in self.adjacency_matrix[x][y].adjacency_list)
            #     or (self.adjacency_matrix[x + 1][y + 1].valid_connections()
            #     and self.adjacency_matrix[x + 1][y + 1] in self.adjacency_matrix[x][y].adjacency_list)):
            #     # print("entre aqui3")
            #     return True
            
        elif in_row:
            # y - 1
            if self.adjacency_matrix[x - 1][y - 1] in self.adjacency_matrix[x][y - 1].adjacency_list:
                return True
            elif self.adjacency_matrix[x + 1][y - 1] in self.adjacency_matrix[x][y - 1].adjacency_list:
                return True
            # y + 1
            elif self.adjacency_matrix[x - 1][y + 1] in self.adjacency_matrix[x][y + 1].adjacency_list:
                return True
            elif self.adjacency_matrix[x + 1][y + 1] in self.adjacency_matrix[x][y + 1].adjacency_list:
                return True

        return False

    def print_connected_nodes(self):
        print("----SEE CONNECTED NODES----")
        for node in self.connected_nodes:
            print(f"Adjacent nodes of {node}:", end=" ")
            for adjacent in node.adjacency_list:
                print(adjacent, end=" ")
            print()
        print()

    def print_graph(self):
        print("----SEE GRAPH----")
        for row in self.adjacency_matrix:
            for cell in row:
                print(f"Adjacent nodes of {cell}:", end=" ")
                for node in cell.adjacency_list:
                    print(node, end=" ")
                print()
            print()

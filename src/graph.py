from src.node import Node


class Graph:
    def __init__(self, file_name) -> None:
        self.all_nodes = []
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
        self.print_graph()
        self.print_connected_nodes()
        res = self.is_cyclic()
        return res

        # def dfs(self, current_node, visited, parent_node):
        # print(f"Visiting node: {current_node}")
        # visited.append(current_node)

        # # # Validate the node based on its color
        # # if current_node.color == 1:  # White
        # #     print("Node is white, checking validity...")
        # #     if not self.check_valid_white(current_node):
        # #         print("Node is not valid, returning False")
        # #         return False
        # #     print("Node is valid")

        # # elif current_node.color == 2:  # Black
        # #     print("Node is black, checking validity...")
        # #     if not self.check_valid_black(current_node):
        # #         print("Node is not valid, returning False")
        # #         return False
        # #     print("Node is valid")
        # # else:
        # #     if not current_node.valid_connections():
        # #         print("Node has no valid connections, returning False")
        # #         return False
        # #     print("Node is valid")

        # for adjacent_node in current_node.adjacency_list:
        #     if adjacent_node not in visited:
        #         print(f"Node {adjacent_node} is not visited, visiting it...")
        #         if self.dfs(adjacent_node, visited, current_node) is True:
        #             return True
        #     elif adjacent_node != parent_node:
        #         print("Found a cycle, returning True")
        #         return True

        # print("Finished visiting all adjacent nodes, returning False")
        # return False

    def dfs(self, current_node, visited, parent_node):
        print(f"Visiting node: {current_node}")
        visited.append(current_node)

        # Validate the node based on its color
        if current_node.color == 1:  # White
            print("Node is white, checking validity...")
            if not self.check_valid_white(current_node):
                print("Node is not valid, returning False")
                return False
            print("Node is valid")

        elif current_node.color == 2:  # Black
            print("Node is black, checking validity...")
            if not self.check_valid_black(current_node):
                print("Node is not valid, returning False")
                return False
            print("Node is valid")
            
        for adjacent_node in current_node.adjacency_list:
            if adjacent_node not in visited:
                print(f"Node {adjacent_node} is not visited, visiting it...")
                if self.dfs(adjacent_node, visited, current_node) is True:
                    return True
            elif adjacent_node != parent_node:
                print("Found a cycle, returning True")
                return True
    
        print("Finished visiting all adjacent nodes, returning False")
        return False
    
    def is_cyclic(self):
        if not self.all_valid_connections():
            return False
    
        self.get_connected_nodes()
    
        for node in self.connected_nodes:
            visited = []  # Clear the visited list for each new starting node
            # Validate the node based on its color
            if node.color == 1:  # White
                print("Node is white, checking validity...")
                if not self.check_valid_white(node):
                    print("Node is not valid, returning False")
                    return False
                print("Node is valid")
            elif node.color == 2:  # Black
                print("Node is black, checking validity...")
                if not self.check_valid_black(node):
                    print("Node is not valid, returning False")
                    return False
                print("Node is valid")
            print(f"Node {node} is not visited, starting DFS...")
            if self.dfs(node, visited, None) is True:
                print("Found a cycle, graph is cyclic")
                return True
    
        print("Finished visiting all nodes, no cycles found")
        return False
    
    def check_valid_black(self, node: Node) -> bool:
        """
        Check if the black node is valid or not
        """
        valid = False
        if node.valid_connections():
            if self.check_adyacent_black(node.x, node.y):
                valid = True

        return valid

    def check_valid_white(self, node: Node) -> bool:
        """check if the black node is valid or not
        """
        valid = False
        # print("fasfda", self.adjacency_matrix[x][y].weight)
        if node.valid_connections():
            if self.check_adyacent_white(node.x, node.y):
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

        # check down
        if (0 <= (x + 1) <= (self.size - 2)):
            print("check down")
            if (self.adjacency_matrix[x + 1][y].valid_connections()
                    and self.adjacency_matrix[x + 2][y].valid_connections()):
                pos_adyacent.append(1)

        # check left
        if (2 <= (y + 1) <= self.size):
            print("check left")
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                    and self.adjacency_matrix[x][y - 2].valid_connections()):
                pos_adyacent.append(2)

        # check right
        if (0 <= (y + 1) <= (self.size - 2)):
            print("check right")
            if (self.adjacency_matrix[x][y + 1].valid_connections()
                and self.adjacency_matrix[x][y + 2].valid_connections()
                    and not 2 in pos_adyacent):
                pos_adyacent.append(3)

        # check up
        if (2 <= (x + 1) <= self.size):
            print("check up")
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
                
            if (self.adjacency_matrix[x][y - 1].valid_connections()
                    and self.adjacency_matrix[x][y + 1].valid_connections()):
                # print("entre aquia")
                in_row = True

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
        if in_column or in_row:
            # print("entre aqui2")
            # check connection turn to a column or row
            # check left
            if (self.adjacency_matrix[x - 1][y - 1].valid_connections()
                or self.adjacency_matrix[x + 1][y - 1].valid_connections()
                or self.adjacency_matrix[x - 1][y + 1].valid_connections()
                    or self.adjacency_matrix[x + 1][y + 1].valid_connections()):
                # print("entre aqui3")
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
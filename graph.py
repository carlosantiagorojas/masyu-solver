from node import Node


class Graph:
    def __init__(self, file_name) -> None:
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
                adjacency_matrix[row - 1][col - 1] = Node(color)
        
        return adjacency_matrix
    
    def add_edge(self, s_row: int, s_column: int, e_row: int, e_column: int) -> None:
        """
        Add an edge between two nodes
        """
        # Implement logic
        pass
    
    def win(self) -> bool:
        """
        Check if the game is over, this is when the graph is cyclic
        """
        # Implement logic
        return False
    
    def __str__(self) -> str:
        matrix_str = "-" * 37 + "\n"
        for i in range(self.size):
            matrix_str += "|"
            for j in range(self.size):
                node = self.adjacency_matrix[i][j]
                if node is not None:
                    if node.color == 1:
                        # Use a Unicode character to represent a black circle
                        matrix_str += " \u25CF ".center(5) + "|"
                    elif node.color == 2:
                        # Use a Unicode character to represent a white circle
                        matrix_str += " \u25CB ".center(5) + "|"
                else:
                    matrix_str += "".center(5) + "|"
            matrix_str += "\n" + "-" * 37 + "\n"
        return matrix_str
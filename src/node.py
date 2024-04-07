from typing import Optional


class Node:
    """
    Node class to represent a node in the graph

    Parameters
    ----------
    color : Optional[int]
        The color of the node
        1 = white
        2 = black
        3 = connection
        None = empty
    value : int
        The weight of the node (default is 0), to know the connections of the node
    left : False
        If the node has a connection to the left
    right : False
        If the node has a connection to the right
    up : False
        If the node has a connection to the up
    down : False
        If the node has a connection to the down

    Methods
    -------

    """
    def __init__(self, color: Optional[int], x: int, y: int) -> None:
        """
        Args:
            color (Optional[int]): The color of the node
            1: White
            2: Black
        """
        self.x = x
        self.y = y
        self.color = color
        self.weight = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def valid_connections(self) -> bool:
        """Check if the node has more than two connections

        Returns:
            bool: _description_
        """
        if 0 < self.weight < 3:
            return True
        return False
        
    
    # def __str__(self) -> str:
    #     return str(self.color)
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

    def __init__(self, color: Optional[int]) -> None:
        """
        Args:
            color (Optional[int]): The color of the node
        """
        self.color = color
        self.weight = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def __str__(self) -> str:
        return str(self.color)
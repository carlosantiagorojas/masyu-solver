from typing import Optional


class Node:
    def __init__(self, color: Optional[int]) -> None:
        """
        Args:
            color (Optional[int]): The color of the node
            1 = white
            2 = black
            None = empty
        """
        self.color = color
        self.value = 0
    
    def __str__(self) -> str:
        return str(self.color)
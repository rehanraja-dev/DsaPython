from typing import Optional
class Node:
    left : Optional[None]
    right: Optional[None]
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)

root.left = Node(2) 
root.right = Node(3)
        
print(root.left.data)
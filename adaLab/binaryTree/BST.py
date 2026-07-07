from typing import Optional

class Node:
    def __init__(self, item: int):
        self.key = item
        self.left: Optional[None]
        self.right: Optional[None]

def insert(node: Node | None, key: int) -> Node:
    # If the tree/sub-tree is empty, return a new node
    if node is None:
        return Node(key)
        
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key) #type: ignore
    elif key > node.key:
        node.right = insert(node.right, key)  #type: ignore
        
    return node

def search(root: Node | None, key: int) -> Node | None:
    if root is None or root.key == key:
        return root
        
    if root.key < key:
        return search(root.right, key)
        
    return search(root.left, key)

if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 40)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    insert(root, 40)

    key = 6
    if search(root, key) is None:
        print(f"{key} Not found")
    else:
        print(f"{key} found")

    key = 60
    if search(root, key) is None:
        print(f"{key} Not found")
    else:
        print(f"{key} found")

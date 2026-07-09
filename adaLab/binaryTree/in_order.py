class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    def iterative_inorder(self, root):
        stack = []
        curr = root

        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print(curr.data, end=" ")            
            curr = curr.right
            


n = int(input("Enter the number of nodes: "))
root = None

for _ in range(n):
    data = int(input("Enter the data for the node: "))
    if root is None:
        root = Node(data)
    else:
        root = root.insert(root, data)

if root:
    root.iterative_inorder(root)
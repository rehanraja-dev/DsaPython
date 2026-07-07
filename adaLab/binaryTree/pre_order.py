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

    def iterative_preorder(self, root):
        if root is None:
            return

        stack = [root]

        while stack:
            curr = stack.pop()
            print(curr.data, end=" ")

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)


n = int(input("Enter the number of nodes: "))
root = None

for _ in range(n):
    data = int(input("Enter the data for the node: "))
    if root is None:
        root = Node(data)
    else:
        root = root.insert(root, data)

if root:
    root.iterative_preorder(root)
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = "red"

class Tree:
    def __init__(self,data):
        self.root=Node(data)


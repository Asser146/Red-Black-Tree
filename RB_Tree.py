class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = "red"


class Tree:
    def __init__(self):
        self.nil = TreeNode(None)
        self.nil.color = "black"
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, data):
        flag = self.search(self.root, data)
        if flag is True:
            print("ERROR: Word already in the dictionary!")
            return

        newNode = TreeNode(data)
        newNode.parent = None
        newNode.left = self.nil
        newNode.right = self.nil
        newNode.color = "red"
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if newNode.data < current.data:
                current = current.left
            elif newNode.data > current.data:
                current = current.right
            else:
                return

        newNode.parent = parent
        if parent == None:
            self.root = newNode
        elif newNode.data < parent.data:
            parent.left = newNode
        else:
            parent.right = newNode

        if newNode.parent == None:
            newNode.color = "black"
            return

        if newNode.parent.parent == None:
            return

        self.fixInsertion(newNode)

    def fixInsertion(self, newNode):
        while newNode != self.root and newNode.parent.color == "red":
            if newNode.parent == newNode.parent.parent.right:
                uncle = newNode.parent.parent.left  # uncle
                if uncle.color == "red":
                    uncle.color = "black"
                    newNode.parent.color = "black"
                    newNode.parent.parent.color = "red"
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.left:
                        newNode = newNode.parent
                        self.rotateRight(newNode)
                    newNode.parent.color = "black"
                    newNode.parent.parent.color = "red"
                    self.rotateLeft(newNode.parent.parent)
            else:
                uncle = newNode.parent.parent.right  # uncle

                if uncle.color == "red":
                    uncle.color = "black"
                    newNode.parent.color = "black"
                    newNode.parent.parent.color = "red"
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        self.rotateLeft(newNode)
                    newNode.parent.color = "black"
                    newNode.parent.parent.color = "red"
                    self.rotateRight(newNode.parent.parent)
        self.root.color = "black"

    def getHeight(self, node):

        if node == self.nil:
            return -1
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        return max(leftHeight, rightHeight) + 1

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def printInorder(self, node):
        if node:
            self.printInorder(node.left)
            if node != self.nil:
                print(f"Data= {node.data} , color= {node.color}")
            self.printInorder(node.right)

    def search(self, node, data):
        if (node.data == None):
            # print("Not Found")
            return False
        elif (node.data == data):
            print("Found")
            return True
        elif data < node.data:
            if node.left is None:
                return False
            else:
                # print("Went left")
                self.search(node.left, data)
        else:
            if node.right is None:
                return False
            else:
                # print("Went right")
                self.search(node.right, data)

    def treeSize(self, node):
        if node.data == None:
            return 0
        else:
            return self.treeSize(node.left) + 1 + self.treeSize(node.right)

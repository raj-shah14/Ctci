# implementing in-order,pre-order and post-order tree traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# insert Node
    def insert(self,data):

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

# Printing the tree
    def printTheTree(self):
        if self.left:
            self.left.printTheTree()
        print(self.data)
        if self.right:
            self.right.printTheTree()
    
    #In Order Tree Traversal
    def inOrder(self,root):
        res = []
        if root:
            res = self.inOrder(root.left)
            res.append(root.data)
            res = res + self.inOrder(root.right)
        return res

    # Pre Order Tree Traversal
    def preOrder(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res

    #Post Order Tree Traversal
    def postOrder(self,root):
        res = []
        if root:
            res = res + self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.data)
        return res
     
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)


# print(root.printTheTree())
print("InOrder: " + str(root.inOrder(root)))
print("Pre Order: " + str(root.preOrder(root)))
print("Post Order: " + str(root.postOrder(root)))

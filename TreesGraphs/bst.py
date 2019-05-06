
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self,root):
        self.root = Node(root)

    def search(self,val):
        return self.search_helper(self.root,val)


    def search_helper(self,start,val):
        if start:
            if start.data == val:
                return True
            elif start.data > val:
                return self.search_helper(start.left,val)
            else:
                return self.search_helper(start.right,val)
        else:
            return False



    def insert(self, new_val):
        self.insert_node(self.root,new_val)
        
    
    def insert_node(self,start,val):
        if start.data > val:
            if start.left:
                self.insert_node(start.left,val)
            else:
                start.left = Node(val)
        else:
            if start.right:
                self.insert_node(start.right,val)
            else:
                start.right = Node(val)

    

    def preOrder(self):
        return self.preOrder_(self.root,"")[:-1]

    # helper
    def preOrder_(self,start,traversal):
        if start:
            traversal += (str(start.data)+"-")
            traversal = self.preOrder_(start.left,traversal)
            traversal = self.preOrder_(start.right,traversal)
        return traversal

    def inOrder(self):
        return self.inOrder_(self.root,"")[:-1]

    #helper
    def inOrder_(self,start,traversal):
        if start:
            traversal = self.inOrder_(start.left,traversal)
            traversal += (str(start.data)+"-")
            traversal = self.inOrder_(start.right,traversal)
        return traversal
        

    def postOrder(self):
        return self.postOrder_(self.root,"")[:-1]

    #helper
    def postOrder_(self,start,traversal):
        if start:
            traversal = self.postOrder_(start.left,traversal)
            traversal = self.postOrder_(start.right,traversal)
            traversal += (str(start.data)+"-")
        return traversal

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# tree.insert(6)
# Should be False
print tree.search(6)

print(tree.preOrder())
print(tree.inOrder())
print(tree.postOrder())
#Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
# You may assume that each node has a link to its parent.

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def next_node(root,node):
    if node.right:
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp.val
    else:
        # Checking path of node from root
        s = root
        par = 0
        while s.val != node.val:
            if node.val <= s.val:
                par = s.val         # Saving parent value
                s = s.left
            else:
                s = s.right
        if par:
            return par
        else:
            return "Its last elemetn"

                                    # Complexity O(h) height of the tree
root = Node(10) 
root.left = Node(5) 
root.right = Node(20) 
root.left.left = Node(2)
root.left.left.right = Node(4)
root.left.left.right.left = Node(3)  
root.left.right = Node(8)
root.left.right.left = Node(7)
root.left.right.left.left = Node(6)
root.left.right.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(25) 

node = root.left.right.left
print(next_node(root,node))
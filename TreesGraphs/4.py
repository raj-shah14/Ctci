# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, 
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    l = get_height(root.left)
    r = get_height(root.right)
    return 1+max(l,r)

def balanced(root):
    if root is None:
        return True

    lh = get_height(root.left)
    rh = get_height(root.right)
    if (abs(lh-rh) <= 1) and balanced(root.left) is True and balanced(root.right) is True: 
        return True
    
    return False    #O(n^2) time complexity. Since for height we traverse the entire tree and then to check balance again we traverse



class Height:
    def __init__(self):
        self.height = 0


def isBalanced(root,h):
    if root is None:
        return True

    lh = Height()
    rh = Height()

    l = isBalanced(root.left,lh)
    r = isBalanced(root.right,rh)

    h.height = max(lh.height,rh.height)+1

    if abs(lh.height-rh.height)<=1:
        return l and r

    return False        #Time Complexity O(n) , where n is number of nodes in the Tree


root = Node(1)                      #1
root.left = Node(2)               #2   #3
root.right = Node(3)        
root.left.left = Node(4)        #4
root.left.right = Node(5) 
root.right.left = Node(6) 
root.left.left.left = Node(7) 
# root.left.left.left.left = Node(8) 

h = Height()

print(balanced(root))
print(isBalanced(root,h))
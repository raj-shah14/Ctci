# Validate BST: Implement a function to check if a binary tree is a binary search tree.


# All nodes to the left should be smaller than the root and to the right greater than the root.
# Every node should be within a range.
import math

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# Method using Inorder traversal.
def inorderCheckBST(root,stack):
    if root:
        inorderCheckBST(root.left,stack)
        stack.append(root.val)
        inorderCheckBST(root.right,stack)
    return stack

def checkStack(stack):
    for i in range(1,len(stack)):
        if stack[i-1]>stack[i]:
            return False
    return True                     # O(N) time complexity but O(N) space complexity for array 
                                    # Array is not required


# Efficient method using range (min < root.val < max)
def checkBST(root,minv,maxv):
    if root is None:
        return True
    
    if root.val > maxv or root.val<=minv:
        return False
    
    return checkBST(root.left,minv,root.val) and checkBST(root.right,root.val,maxv)  #O(n) time complexity as all nodes are visited



root = Node(20)                      
root.left = Node(10)                 
root.right = Node(30)
root.left.left = Node(1)
root.left.right = Node(12)

print(checkStack(inorderCheckBST(root,[])))

minv = -math.inf
maxv = math.inf
print(checkBST(root,minv,maxv))
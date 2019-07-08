# Paths with Sum: You are given a binary tree in which each node contains an integer value 
# (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. 
# Root to Leaf Path


class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

def printStack(stack):
    print(stack)


def inOrder(root,target):
    sumval = 0
    stack = []
    inOrder_helper(root,stack,sumval,target)

def inOrder_helper(root,stack,sumval,target):
    if root is None:
        return
    stack.insert(0,root.value)
    sumval += root.value
    if sumval == target:
        printStack(stack)

    inOrder_helper(root.left,stack,sumval,target)
    inOrder_helper(root.right,stack,sumval,target)

    sumval -= stack.pop(0)
    
    
root = Node(10)
root.left = Node(8)
root.right = Node(14)
root.left.left = Node(6)
root.left.right = Node(9)
root.left.left.left = Node(4)
root.left.left.right = Node(7)
root.right = Node(14)
root.right.left = Node(12)
root.right.left.left = Node(11)
root.right.right = Node(15)
root.right.left.right = Node(13)

target = 13
inOrder(root,target)
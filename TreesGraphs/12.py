# Paths with Sum: You are given a binary tree in which each node contains an integer value 
# (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. 
# The path does not need to start or end at the root or a leaf, but it must go downwards 
# (traveling only from parent nodes to child nodes)

class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None


def printpath(path,i):
    for j in range(i,len(path)):
        print(path[j]),
    print

def pathSum(root,target):
    path = []
    path_sum_helper(root,path,target)

def path_sum_helper(root,path,target):
    if root is None:
        return
    
    path.append(root.value)

    path_sum_helper(root.left,path,target)
    path_sum_helper(root.right,path,target)

    sumval = 0
    
    for i in range(len(path)-1,-1,-1):
        sumval += path[i]

        if sumval == target:
            printpath(path,i)
    path.pop()
    


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

pathSum(root,18)
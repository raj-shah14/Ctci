# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.

projects = ['a','b','c','d','e','f']
dep = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def values(root):
    stack = [root]

    while stack:
        start = stack.pop()
        print(start.val)
        if start.left:
            stack.append(start.left)
        if start.right:
            stack.append(start.right)
        

root = Node('p')
root.left = Node('e')
root.right = Node('f')
root.right.left = Node('a')
root.right.right = Node('b')
root.right.left.right = Node('d')
root.right.right.left = root.right.left.right
root.right.left.right.left = Node('c')
print(values(root))
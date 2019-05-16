
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def listNodes(root):
    nodes = {}
    lvl = 0
    stack = [(root,lvl)]

    while stack:
        start,lvl = stack.pop(0)

        if lvl not in nodes:
            nodes[lvl] = [start.value]
        else:
            nodes[lvl].append(start.value)

        if start.left is not None:
            stack.append((start.left,lvl+1))
        
        if start.right is not None:
            stack.append((start.right,lvl+1))
    print(nodes)


# Set up tree
root = Node(4)
# Insert elements
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(7)

listNodes(root)
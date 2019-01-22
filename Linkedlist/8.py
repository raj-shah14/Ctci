# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def result(val):
    if val:
        print("There is loop at node {} and value is {}".format(val,val.data))
    else:
        print("No loop detected")

def is_loop(n1):
    if n1 is None:
        return None
    
    nodestack = []
    while n1 is not None:
        if n1 not in nodestack:
            nodestack.append(n1)
        else:
            return n1
        n1 = n1.next
    return None
    
a = Node(14)
b = Node(26)
c = Node(32)
d = Node(23)
e = Node(54)
f = Node(77)
g = Node(44)
h = Node(89)

#Loop is present
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = c

result(is_loop(a))
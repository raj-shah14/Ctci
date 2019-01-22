# Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def intersect(n1,n2):
    curA, curB = n1, n2
    begin, tailA, tailB = None, None, None
    while curA and curB:
        
        if curA == curB:
            begin = curA
            break

        if curA.next:
            curA = curA.next
        elif tailA is None:
            tailA = curA
            curA = n2
        else:
            break

        if curB.next:
            curB = curB.next
        elif tailB is None:
            tailB = curB
            curB = n1
        else:
            break

    return begin

def result(res):
    if res is None:
        print("Linkedlist don't intersect")
    else:  
        print("The intersecting node is {} and value is {}".format(res,res.data))

# Intersecting Example
a = Node(14)
b = Node(26)
c = Node(32)
d = Node(23)
e = Node(54)
f = Node(77)

q = Node(12)
g = Node(44)
h = Node(89)
i = Node(52)
k = Node(22)
m = Node(80)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = i
i.next = k

q.next = g
g.next = h
h.next = f

print("Case 1:")
result(intersect(a,q))

#Non intersecting Example
a.next = b
b.next = c
c.next = d
d.next = e

q.next = g
g.next = h
h.next = m

print("Case 2:")
result(intersect(a,q))

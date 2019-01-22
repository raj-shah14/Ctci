# Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def getlengthandtail(node):
    count = 0
    while node.next is not None:
        count += 1
        node = node.next
    return count,node

def intersect(n1,n2):               # O(A+B) time and O(1) space, where A,B are length of linked list
    if n1 is None or n2 is None:
        return None

    lenA,tailNodeA = getlengthandtail(n1)
    lenB,tailNodeB = getlengthandtail(n2)

    if tailNodeA != tailNodeB:
        return None

    shorter = n1 if lenA < lenB else n2
    longer = n2 if lenA < lenB else n1

    diff = abs(lenA - lenB)

    for _ in range(diff):
        longer = longer.next

    while shorter is not longer:
        shorter = shorter.next
        longer = longer.next

    return longer

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

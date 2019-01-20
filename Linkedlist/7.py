# Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def makeNode(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printlist(self):
        tmp = self.head
        print("AddedLinkedList [ ",end="")
        while tmp is not None:
            print(str(tmp.data),end="")
            if tmp.next is not None:
                print("->",end="")
            tmp = tmp.next
        print(" ]",end="")
        print()

def length(linkedlist):
    count = 0
    ll = linkedlist.head
    while ll is not None:
        count += 1
        ll = ll.next
    return count

def revLinkedList(linkedlist):
    rev = LinkedList()
    rhead = linkedlist.head
    while rhead is not None:
        rev.makeNode(rhead.data)
        rhead = rhead.next
    return rev


def intersection(l1,l2):

    shorter = l2 if length(l1) > length(l2) else l1
    longer = l1 if length(l1) > length(l2) else l2

    diff = length(longer) - length(shorter)
    
    shorter_node, longer_node = shorter.head, longer.head
    
    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


l1 = LinkedList()
l2 = LinkedList()

l1.makeNode(5)
l1.makeNode(84)
l1.makeNode(35)
l1.makeNode(14)
l1.makeNode(26)
l1.makeNode(21)
l1.makeNode(11)
l1.makeNode(7)
l1.makeNode(88)

l1 = revLinkedList(l1)
l1.printlist()

l2.makeNode(33)
l2.makeNode(99)
l2.makeNode(37)
l2.head.next.next.next = Node(l1.head.next.next.data)
l2.makeNode(55)
l2.makeNode(74)
l2.makeNode(28)

l2 = revLinkedList(l2)
l2.printlist()

print(intersection(l1,l2))

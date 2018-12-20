# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.

from Class_Linkedlist import randomLinkedList

def deleteNode(linkedlist,node_value):
    curr = linkedlist.head
    while curr.next is not None:
        if curr.next.value == node_value:
            curr.next = curr.next.next
            return
        else:
            curr = curr.next
    print('{} value is not in list'.format(node_value))


L1 = randomLinkedList(9,1,8)
print(L1)
deleteNode(L1,5)
print(L1)
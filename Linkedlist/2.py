#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from Class_Linkedlist import randomLinkedList

#Getting the length of Linked List
def getLength(linkedlist):
    count = 0
    head = linkedlist.head
    while head is not None:
        count += 1
        head = head.next
    return count

# getting Kth from the Last
def getKthfromlast(linkedlist,index):
    lenll = getLength(linkedlist)
    if index == 0:
        return "Give index greater than 0"
    if index > lenll:
        return '{}th index is out of bound'.format(index)
    elem = lenll - index 
    curr = linkedlist.head
    while elem > 0:
        curr = curr.next
        elem -= 1
    return curr.value       #O(n) solution


# Deleting Kth from Last
def deleteKthfromlast(linkedlist,index):
    lenll = getLength(linkedlist)
    if index == 0:
        return "Give index greater than 0"
    if index > lenll:
        return '{}th index is out of bound'.format(index)
    elem = lenll - index 
    curr = linkedlist.head
    while elem > 1:
        curr = curr.next
        elem -= 1
    curr.next = curr.next.next


L1 = randomLinkedList(9,2,9)
print(L1)
print(getKthfromlast(L1,6))
deleteKthfromlast(L1,6)
print(L1)
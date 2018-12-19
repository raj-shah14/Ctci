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



#Alternate Solution using Recursion
def getKthWithRecursion(head,index):
    if head is None:
        return 0
    elem = getKthWithRecursion(head.next,index) + 1
    if elem == index:
        print("Recursive Approach: "+ str(head.value))                  #O(n) space due to recursive calls
    return elem


# Alternate Iterative solution, more optimal
def iterativeKthElement(linkedlist,index):
    ptr1 = linkedlist.head
    ptr2 = linkedlist.head
    for _ in range(index):
        if ptr1 is None:
            return None
        ptr1 = ptr1.next

    while ptr1 is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr2.value           # O(n) time and O(1) space.

    #Here i am not counting the length of my Linked list.





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
print("My approach: " + str(getKthfromlast(L1,6)))
print("Iterative 2 pointer appraoch: "+ str(iterativeKthElement(L1,6)))
getKthWithRecursion(L1.head,6)
# deleteKthfromlast(L1,6)
# print(L1)
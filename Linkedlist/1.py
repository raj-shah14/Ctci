#Write code to remove duplicates from an unsorted linked list.

from Class_Linkedlist import randomLinkedList

def delDuplicates(linkedlist):  #O(n^2) solution
    curr = linkedlist.head
    while curr is not None:
        runn = curr
        while runn.next is not None:
            if runn.next.value == curr.value:
                runn.next = runn.next.next
            else:
                runn = runn.next
        curr = curr.next


# Alternate solution

def delDuplicates2(linkedlist):     #O(n) solution
    curval = linkedlist.head
    tempdict = {curval.value : True}
    while curval.next is not None:
        if curval.next.value in tempdict:
            curval.next = curval.next.next
        else:
            tempdict[curval.next.value] = True
            curval = curval.next


L1 = randomLinkedList(9, 3, 7)  #Length, min ,max
print(L1)
delDuplicates(L1)
print(L1)

L2 = randomLinkedList(9, 3, 7)
print(L2)
delDuplicates2(L2)
print(L2)

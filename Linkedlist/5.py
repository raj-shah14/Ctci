# You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

from Class_Linkedlist import randomLinkedList

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def makeNode(self,newdata):
        newNode = Node(newdata)
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



def add_linkedlist(linkedlist1,linkedlist2):
    head1 = linkedlist1.head
    head2 = linkedlist2.head
    carry = 0
    result = []
    while head1 is not None or head2 is not None:
        h1val = 0 if head1 is None else head1.value
        h2val = 0 if head2 is None else head2.value
        temp = h1val + h2val + carry
        carry = 0
        if temp > 9:
            result.append(int(temp%10))
            carry = int(temp/10)
        else:
            result.append(temp)
        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next
    if carry:
        result.append(carry)
    return result



L1 = randomLinkedList(5,1,9)
print(L1)
L2 = randomLinkedList(2,1,9)
print(L2)
results = add_linkedlist(L1,L2)
#print(results)
res = LinkedList()

for i in results[::-1]:
    res.makeNode(i)
res.printlist()
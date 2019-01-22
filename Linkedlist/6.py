#Palindrome: Implement a function to check if a linked list is a palindrome.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def makeNode(self,val):
        newNode = Node(val)
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

def revLinkedList(linkedlist):
    rev = LinkedList()
    length = 0
    rhead = linkedlist.head
    while rhead is not None:
        rev.makeNode(rhead.data)
        length += 1
        rhead = rhead.next
    return rev,length


def checkPalindrome(linkedlist):            #Using bits
    head = linkedlist.head
    alpha = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    bits = [0 for _ in range(26)]
    while head is not None:
        if head.data in alpha.keys():
            if bits[alpha[head.data]] == 1:
                bits[alpha[head.data]] = 0
            elif bits[alpha[head.data]] == 0:
                bits[alpha[head.data]] = 1
        head = head.next
    if sum(bits) == 1 or sum(bits) == 0:
        return True
    return False


def checkPalCompare(l1,l2,size):        #Using size, linkedlist and reverse of linkedlist upto center value
    first = l1.head
    sec = l2.head
    for _ in range(0,int(size/2)):
        while first is not None and sec is not None:
            if first.data != sec.data:
                return False
            first = first.next
            sec = sec.next
    return True


def is_palindrome(linkedlist):
    fast = slow = linkedlist.head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:                    # Incase of the list is odd, move to next value after reaching middle
        slow = slow.next

    while slow:
        top = stack.pop()
        if top != slow.data:
            return False

        slow = slow.next 
    return True



l1 = LinkedList()

l1.makeNode('A')
l1.makeNode('B')
l1.makeNode('C')
l1.makeNode('D')
l1.makeNode('D')
l1.makeNode('C')
l1.makeNode('B')
l1.makeNode('A')

l2,lllength = revLinkedList(l1)
print("First List")
l1.printlist()

print("Reverse List")
l2.printlist()
print("Is the list Palindrome? Result: {}".format(checkPalindrome(l1)))
print("Result via Compare: {}".format(checkPalCompare(l1,l2,lllength)))         # O(n/2) complexity for time

print("Result via Stack: {}".format(is_palindrome(l1)))
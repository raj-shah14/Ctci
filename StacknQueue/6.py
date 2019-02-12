# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked List data structure.

import random

class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def makeNode(self,data):
        newNode = Node(data)
        if self.tail is not None:
            self.tail.next = newNode
        self.tail = newNode    
        if self.head is None:
            self.head = self.tail
        
        
    def removeNode(self):
        dat = None
        if self.head is not None:
            dat = self.head.value
            self.head = self.head.next
            return dat
        else:
            self.tail = None
            return dat
    
    def peek(self):
        if self.head:
            return self.head.value


    def printlist(self):
        tmp = self.head
        print("AddedLinkedList [ ",end="")
        while tmp is not None:
            print(str(tmp.value),end="")
            if tmp.next is not None:
                print("->",end="")
            tmp = tmp.next
        print(" ]",end="")
        print()


def enqueue(shelter):
    enqc = Linkedlist()
    enqd = Linkedlist()
    for i in shelter:
        if i.startswith("C"):
            enqc.makeNode(i)
        if i.startswith("D"):
            enqd.makeNode(i)
    return enqc,enqd


def dequeueAny(linkedlistc,linkedlistd):
    dqac = linkedlistc
    dqad = linkedlistd
    ra = random.randint(1,2)
    if ra == 1:
        order = dqac.removeNode()
    else:
        order = dqad.removeNode()
    return order


def dequeueCat(linkedlist):
    dqc = linkedlist
    first = dqc.removeNode()
    return first

def dequeueDog(linkedlist):
    dqd = linkedlist
    dog = dqd.removeNode()
    return dog
    

shelter = ["Dog1", "Cat1","Dog2","Dog3","Cat2","Dog4","Dog5","Cat3","Cat4","Cat5","Dog6","Dog7","Dog8","Cat6" ]

enqc,enqd = enqueue(shelter)
enqc.printlist()
enqd.printlist()

print(dequeueAny(enqc,enqd))
print(dequeueDog(enqd))
print(dequeueCat(enqc))

enqc.printlist()
enqd.printlist()
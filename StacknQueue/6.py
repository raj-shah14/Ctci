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




enqueue = Linkedlist()


enqueue.makeNode("Dog1")
enqueue.makeNode("Cat1")
enqueue.makeNode("Dog2")
enqueue.makeNode("Dog3")
enqueue.makeNode("Cat2")
enqueue.makeNode("Dog4")
enqueue.makeNode("Dog5")
enqueue.makeNode("Cat3")
enqueue.makeNode("Cat4")
enqueue.makeNode("Cat5")
enqueue.makeNode("Dog6")
enqueue.makeNode("Dog7")
enqueue.makeNode("Dog8")
enqueue.makeNode("Cat6")


enqueue.printlist()
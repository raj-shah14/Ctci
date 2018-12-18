

############################### Setting up linkedlist ######################
from random import randint

class Node:
    def __init__(self,value,nextNode = None):
        self.value = value
        self.next = nextNode


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        node = Node(value)

        #IF first node
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"





def randomLinkedList(length, min, max):
    linkedlist = Linkedlist()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist
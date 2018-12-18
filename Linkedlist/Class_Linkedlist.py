

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
        #New Node is head node
        node = Node(value,self.head)
        self.head = node

        #IF first node
        # if self.head == None:
        #     self.head = node
        #     self.tail = node
        # else:
        #     self.tail.next = node
        #     self.tail = node

    def removeNode(self,node_value):
        curr = self.head
        if curr.value == node_value:
            self.head = self.head.next
        while curr.next is not None:
            if curr.next.value == node_value:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next

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
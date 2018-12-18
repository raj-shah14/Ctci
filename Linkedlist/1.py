#Write code to remove duplicates from an unsorted linked list.

############################### Setting up linkedlist ######################

def getLinkedList():
    class Node:
        def __init__(self,value,nextNode = None):
            self.value = value
            self.next = nextNode
    

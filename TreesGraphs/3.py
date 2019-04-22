# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self,head):
        self.head = head
        self.next = None




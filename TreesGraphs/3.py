# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Linkedlistnode:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self,value):
        #New Node is head node
        node = Linkedlistnode(value,self.head)
        self.head = node
    
    def printLL(self):
        index = self.head
        print("New List")
        print(str(index.val))
        while index.next is not None:
            index = index.next
            print(index.val),
        

def listOfDepths(root):
        nodes = {}
        lvl = 1
        stack = [(root,lvl)]

        while stack:
            start,lvl = stack[0]
            stack = stack[1:]

            if start:
                if lvl not in nodes:
                    nodes[lvl] = [start.value]
                else:
                    nodes[lvl].append(start.value)

                if start.left:
                    stack.append((start.left,lvl+1))
                if start.right:
                    stack.append((start.right,lvl+1))
        return nodes


def arrToll(arr):
    ll = LinkedList()
    for i in range(0,len(arr)):
        ll.addNode(arr[i])
    ll.printLL()
    return ll

# Set up tree
root = Node(4)
# Insert elements
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(5)


lists = listOfDepths(root)
for i in lists.values():
    arrToll(i)
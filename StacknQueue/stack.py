# Implementing a Stack.
#  Last in First out (LIFO)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def pop(self):
        val = None
        if self.top is not None:
            val = self.top.data
            self.top = self.top.next
        return val 
    
    def push(self,value):
        newval = Node(value)
        newval.next = self.top
        self.top = newval
        

    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top == None



s = Stack()
print("Is Stack Empty? {}".format(s.isEmpty()))
print("Pushing Elements in Stack")
s.push(10)
s.push(21)
s.push(14)
s.push(63)
s.push(56)

print("Is Stack Empty? {}".format(s.isEmpty()))
print("Checking top of Stack: {}".format(s.peek()))
print("Popping the top of the stack value: {}".format(s.pop()))
print("Again Checking top of Stack: {}".format(s.peek()))

print("----------------------------------")
# Implementing a Queue
# First In First Out

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self,value):
        newnode = Node(value)
        if self.last is not None:
            self.last.next = newnode
        self.last = newnode
        if self.first is None:
            self.first = self.last

    def remove(self):
        dat = None
        if self.first is None:
            self.last = None
            return dat
        dat = self.first.data
        self.first = self.first.next
        return dat

    def peek(self):
        if self.first is not None:
            return self.first.data

    def isEmpty(self):
        return self.first == None

q = Queue()
print("Is Queue Empty? {}".format(q.isEmpty()))
print("Adding in Queue")
q.add(10)
q.add(20)
q.add(30)
q.add(40)
q.add(50)
print("Is Queue Empty? {}".format(q.isEmpty()))
print("Check the first Element: {}".format(q.peek()))
print("Remove the first Element: {}".format(q.remove()))
print("Again, Checking the first Element: {}".format(q.peek()))
print("Remove the first Element: {}".format(q.remove()))
print("Again, Checking the first Element: {}".format(q.peek()))
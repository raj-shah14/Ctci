# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.

class Stack:
    def __init__(self,thresh):
        self.thresh = thresh
        self.arr = []

    def push(self,value):
        self.value = value
        self.arr.insert(0,self.value)
    

    def isFull(self):
        return len(self.arr) == self.thresh


    def pop(self):
        top = self.arr[0]
        del self.arr[0]
        return top
    
    def isEmpty(self):
        return self.arr == []

    def peek(self):
        return self.arr[0]

    def showStack(self):
        print(self.arr)


class SOP:
    def __init__(self):
        self.setofstacks = []

    def push(self,Stack):
        self.Stack = Stack
        self.setofstacks.insert(0,self.Stack)

    def showsop(self):
        print(self.setofstacks)
    
s = Stack(5)
s.push(5)
s.push(10)
s.push(23)
s.push(24)
s.push(6)

print(s.isFull())
s.showStack()
sop = SOP()
sop.push(s)

sop.showsop()
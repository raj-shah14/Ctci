# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

class Stack:
    def __init__(self):
        self.arr = []

    def push(self,val):
        self.arr.insert(0,val)

    def pop(self):
        popval = self.arr[0]
        del self.arr[0]
        return popval

    def top(self):
        return self.arr[0]
    
    def isEmpty(self):
        return self.arr == []


    def showstack(self):
        print(self.arr)


def sortStack(inputStack):          # O(n^2) time Complexity and O(n) space Complexity
    tmpStack = Stack()
    while not inputStack.isEmpty():
        tmp = inputStack.pop()
        while not tmpStack.isEmpty() and tmpStack.top() > tmp:
            inputStack.push( tmpStack.top() )    
            tmpStack.pop()
    
        tmpStack.push(tmp)
    return tmpStack        

s = Stack()
s.push(10)
s.push(3)
s.push(5)
s.push(8)
s.push(1)

s.showstack()
res = Stack()
res = sortStack(s)
res.showstack()
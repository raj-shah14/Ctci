# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.

class StackofPlates:
    def __init__(self,thresh):
        self.thresh = thresh        #capacity of stack
        self.setOfStacks = []       #Main stack
    
    def isFull(self):               #Check if substack is full
        return len(self.setOfStacks[0]) == self.thresh

    def isEmpty(self):              # check if main stack is empty
        return self.setOfStacks == []

    def push(self,value):
        self.value = value
        if self.isEmpty():
            self.setOfStacks.insert(0,[self.value])     # If main stack empty push at first index a list
        else:
            if self.isFull():                           # If sub stack at its full capacity make new stack
                self.setOfStacks.insert(0,[self.value])
            else:
                self.setOfStacks[0].insert(0,self.value) # else insert into the existing stack

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            if len(self.setOfStacks[0]) == 1:           # if substack has just one element, pop and delete sub stack
                popval = self.setOfStacks[0][0]
                del self.setOfStacks[0]
            else:
                popval = self.setOfStacks[0][0]         # Else return and delete value
                del self.setOfStacks[0][0]
            return popval
        
    def showStack(self):
        print(self.setOfStacks)

    def popAt(self,idx):                #index starts from zero
        if self.isEmpty():
            return "Stack is Empty"
        else:
            if len(self.setOfStacks[0]) == 1:
                if idx != 0:
                    return "index not found"
                else:
                    retval = self.setOfStacks[0][idx] 
                    del self.setOfStacks[0]
                    return retval
            else:
                if len(self.setOfStacks[0]) -1 < idx:
                    return "Value not found"
                else:
                    retval = self.setOfStacks[0][idx] 
                    del self.setOfStacks[0][idx]
                    return retval

sop = StackofPlates(5)
sop.push(5)
sop.push(6)
sop.push(7)
sop.push(8)
sop.push(9)
sop.push(1)
sop.push(2)
sop.push(3)
sop.push(4)
sop.push(10)
sop.push(11)
sop.push(12)

sop.showStack()
print(sop.pop())
sop.showStack()
print(sop.pop())
sop.showStack()
print(sop.pop())
sop.showStack()
print(sop.pop())
sop.showStack()
print(sop.pop())
sop.showStack()

sop.push(52)
sop.push(33)
sop.push(51)
sop.push(50)
sop.push(37)


print(sop.popAt(1))
sop.showStack()

print(sop.popAt(0))
sop.showStack()

print(sop.popAt(2))
sop.showStack()
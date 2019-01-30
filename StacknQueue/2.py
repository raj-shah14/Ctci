# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class minStack:
    def __init__(self):
        self.arr = []
        self.MIN = 9999

    def setMin(self):
        for i in self.arr:
            if i < self.MIN:
                self.MIN = i
        

    def getMin(self):
        return self.MIN

    def push(self,value):
        self.value = value
        self.arr = [self.value] + self.arr
        if self.value < self.MIN:
            self.setMin()

    def pop(self):
        val = self.arr[0]
        del self.arr[0]
        if val == self.MIN:
            self.MIN = self.arr[0]
            self.setMin()
        return val

    def showStack(self):
        return self.arr

m = minStack()
m.push(5)
m.push(14)
m.push(95)
m.push(1)

print("The stack is: {}".format(m.showStack()))
print("The min in Stack is: {}".format(m.getMin()))

print("Popping the top of Stack: {}".format(m.pop()))

print("The Stack now: {}".format(m.showStack()))
print("The min in Stack is: {}".format(m.getMin()))

m.push(2)
print("The stack is: {}".format(m.showStack()))
print("The min in Stack is: {}".format(m.getMin()))

m.push(1)
m.push(100)
m.push(85)

print("Popping the top of Stack: {}".format(m.pop()))

print("The stack is: {}".format(m.showStack()))
print("The min in Stack is: {}".format(m.getMin()))
# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class minStack:
    def __init__(self):
        self.arr = []
        

    def push(self,value):
        self.value = value
        self.arr = [self.value] + self.arr

    def getMin(self):
        self.MIN = 9999
        for i in self.arr:
            if i < self.MIN:
                self.MIN = i
        print(self.MIN)

    def pop(self):
        val = self.arr[0]
        print(val)
        del self.arr[0]

    def showStack(self):
        print(self.arr)

m = minStack()
m.push(5)
m.push(14)
m.push(95)
m.push(1)

m.getMin()
m.showStack()
m.pop()

m.pop()
m.getMin()
m.showStack()

m.pop()
m.showStack()
# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self,value):
        self.stack1.insert(0,value)

    def remove(self):
        val = self.stack1[0]
        self.stack2.insert(0,val)
        del self.stack1[0]

    def showQueue(self):
        print(self.stack2)

    def size(self):
        return len(self.stack1)



m = MyQueue()
m.add(1)
m.add(2)
m.add(3)
m.add(4)
m.add(5)

for i in range(m.size()):           # O(n) depends on size of queue
    m.remove()

m.showQueue()

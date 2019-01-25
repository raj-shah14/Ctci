
# Three in One: Describe how you could use a single array to implement three stacks

class Kstacks:
    def __init__(self,n,k):
        self.n = n          # Number of elements in Stack
        self.k = k          # Number of stacks
        self.arr = [0]*self.n   # Size of array

        self.top = [-1] * self.k  # Gives top of stack for each stack
                                  #-1 says no value in stack
        self.next = [i+1 for i in range(self.n)]
        self.next[self.n -1] = -1

        self.free = 0       # top of free stack

    def isEmpty(self,sn):           #Checks if the Stack is Empty
        return self.top[sn] == -1

    def isFull(self):
        return self.free == -1
    
    def push(self,sn,val):

        if self.isFull():
            print("Stack Overflow")
            return 

        # Position to insert
        insert_at = self.free

        # Adjust the next free element
        self.free = self.next[self.free]

        #Insert the value in array
        self.arr[insert_at] = val

        # when we pop we want next to point previous value too
        self.next[insert_at] = self.top[sn]

        # Update top of stack
        self.top[sn] = insert_at

    def pop(self,sn):
        pop_from = self.top[sn]
        self.top[sn] = self.next[self.top[sn]]
        self.next[pop_from] = self.free 
        self.free = pop_from 
  
        return self.arr[pop_from] 
  
    
k = Kstacks(15,3)
k.push(0,5)
k.push(0,6)
k.push(0,14)

k.push(1,8)
k.push(1,15)

k.push(2,10)
k.push(2,11)

print(k.pop(0))
print(k.pop(1))
print(k.pop(2))
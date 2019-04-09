# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo-
# rithm to create a binary search tree with minimal height.

arr = [10,12,15,16,22,24,35,36,48,50,56,63,66,70,75]
mid = int(len(arr)/2)

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'

def initiate(arr):
    '''
    inp: arr
    '''
    return findMid(arr,0,len(arr)-1)            # Initializing recursion call


def findMid(arr,start,end):         # Starting and Ending point of array
    '''
    @param: arr :sorted
    int : start
    int : end
    '''
    if start > end:                 # Base case
        return ''
    mid = int((start + end )/2)
    root = Node(arr[mid])
    root.left = findMid(arr,start,mid-1)        #left subtree
    root.right = findMid(arr,mid+1,end)         #right subtree
    return root

print(initiate(arr))


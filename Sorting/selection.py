# Implementation of selection Sort

arr = [14,22,34,10,32,99,43,76,8,40]

# Step 1 - Find Min element
for i in range(0,len(arr)):
    MIN = i

    #Compare with other element and place it at first
    for j in range(i+1,len(arr)):
        if arr[j] < arr[MIN]:
            MIN = j

    arr[i],arr[MIN] = arr[MIN],arr[i]

print(arr)        
        

#Selection Sort

def swap(arr,val1,val2):
  temp = arr[val1]
  arr[val1] = arr[val2]
  arr[val2] = temp
  return arr

def indexofMin(arr,start):
  minval = arr[start]
  idx = start

  for i in range(idx+1,len(arr)):
    if arr[i] < minval:
      minval = arr[i]
      idx = i
  return idx

def selectionSort(arr):
  for i in range(len(arr)):
    rs = indexofMin(arr,i)
    swap(arr,rs,i)
  
  return arr

print(selectionSort(arr))
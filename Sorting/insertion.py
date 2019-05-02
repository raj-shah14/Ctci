# Implementation of Insertion sort

arr = [14,22,34,10,32,99,43,76,8,40]

for i in range(1,len(arr)):
    hole = i
    val = arr[hole]

    while hole > 0 and arr[hole-1] > val:
        arr[hole] = arr[hole-1]
        hole = hole -1 

    arr[hole] = val

print(arr)

# Insertion sort

def insertionSort(arr):
  for i in range(1,len(arr)):
    hole = i
    val = arr[hole]

    while hole>0 and arr[hole-1]>val:
      arr[hole-1]=arr[hole]
      hole = hole-1

    arr[hole] = val
  
  print(arr)

insertionSort(arr)
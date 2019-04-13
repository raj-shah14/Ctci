# Implementation of Bubble Sort

arr = [14,22,34,10,32,99,43,76,8,40]

for i in range(len(arr)):
    for j  in range(len(arr)-i-1):
        if arr[j+1]< arr[j]:
            arr[j+1],arr[j] = arr[j],arr[j+1]

print(arr)
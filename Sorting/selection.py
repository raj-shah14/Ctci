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
        
# Implementation of Quick Sort

# Partition the array into 4 Parts
# L: left of Pivot
# G: right of Pivot
# U: element yet to be sorted
# P: Pivot element


# partition(arr[p...r])
# arr[p .. q-1] , arr[q] , arr[q+1 .. r-1] , arr[r]

arr = [56,2,14,85,3,45,8,78,-12,-45,0,14]

def partition(arr,p,r):
    q = p  #starting point for G: Right of pivot
    pivot = arr[r]
    for j in range(p,r):
        if (arr[j]<=pivot):
            arr[j],arr[q] = arr[q],arr[j]
            q+=1
    arr[r],arr[q] = arr[q],arr[r]    #Swapping pivot point with first value of G inorder to have pivot in between.
    return q

def quickSort(arr,p,r):
    if p<r:
        q = partition(arr,p,r)
        quickSort(arr,p,q-1)
        quickSort(arr,q+1,r)  


quickSort(arr,0,len(arr)-1)
print(arr)
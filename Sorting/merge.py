# merge Sort

arr3 = [56,2,14,85,3,45,8,78]

def merge(arr,p,q,r):
  lowHalf = arr[p:q+1]
  highHalf = arr[q+1:r+1]

  k = p
  i,j = 0,0

  while (i<len(lowHalf) and j<len(highHalf)):
    if lowHalf[i] < highHalf[j]:
      arr[k] = lowHalf[i]
      i = i+1
    else:
      arr[k] = highHalf[j]
      j = j+1
    k = k+1
  
  while i<len(lowHalf):
    arr[k] = lowHalf[i]
    i+=1
    k+=1

  while j<len(highHalf):
    arr[k] = highHalf[j]
    j+=1
    k+=1

def mergeSort(arr,p,r):
  if p<r:
    q = int((p+r)/2)
    mergeSort(arr,p,q)
    mergeSort(arr,q+1,r)
    merge(arr,p,q,r)

mergeSort(arr3,0,len(arr3)-1)
print(arr3)
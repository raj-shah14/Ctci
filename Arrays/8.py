# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to O.


arr = [[1,1,5,4],[2,7,0,4],[0,6,2,8]]
row = [1]*len(arr)
col = [1]*len(arr[0])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            row[i] = 0
            col[j] = 0       

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(row[i] == 0 or col[j] == 0):
            arr[i][j] = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j]),
    print('')               #O(M+N)space  O(MN) time complexity

#Reduced Space approach
print("Reduced Space")

arr = [[1,1,5,4],[2,7,0,4],[0,6,2,8]]
row_flag = False
col_flag = False

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(i == 0 and arr[i][j] == 0):
            row_flag = True
        if(j == 0 and arr[i][j] == 0):
            col_flag = True
        if(arr[i][j] == 0):
            arr[0][j] = 0
            arr[i][0] = 0

for i in range(1,len(arr)):
    for j in range(1,len(arr)+1):
        if(arr[i][0] == 0 or arr[0][j] == 0):
            arr[i][j] = 0
    
if(row_flag):
    for i in range(len(arr)):
        arr[0][i] = 0

if (col_flag):
    for j in range(len(arr)):
        arr[j][0] = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j]),
    print('')                   #O(1) space complexity



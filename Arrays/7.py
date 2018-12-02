#Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees

mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def rotate_mat(mat1):
    N = len(mat1)
    temp = N - 1  
    mat2 = [[0 for i in range(N)] for j in range(N)]
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            mat2[j][temp] = mat1[i][j]
        temp = temp - 1
    return mat2

def rotate_mat_by(mat1,n):
    for _ in range(n):
        mat1 = rotate_mat(mat1)
    return mat1


#Input: Matrix and rotation angle.
mat2 = rotate_mat_by(mat1,1)
#Fot Visualization
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        print(mat1[i][j]),
    print('')

print("After Rotation")

#Visualization after rotation.
#Rotate by 90 degree.

for i in range(len(mat2)):
    for j in range(len(mat2[i])):
        print(mat2[i][j]),
    print('')                   #O(n^2) time and space Complexity
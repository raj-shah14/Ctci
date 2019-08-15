# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

grid = [[1,1,1,1],
        [1,1,0,1],
        [0,1,1,1],
        [1,0,1,"E"]
    ]
# grid = [[1,1],[1,"E"]]

def find_path_helper(grid,i,j,path,visited):
    if i<0  or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0 or visited[i][j]:
        return False
    
    point = (i,j)
    visited[i][j] = True
    if grid[i][j] == "E" or find_path_helper(grid,i+1,j,path,visited) or find_path_helper(grid,i,j+1,path,visited):
        # print("Found Path")
        path.append(point)
        return True
    # find_path_helper(grid,i+1,j,path,visited) 
    # find_path_helper(grid,i,j+1,path,visited)
    return False


def find_path(grid):
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if visited[i][j] or grid[i][j] == 0 or grid[i][j] == "E":
    #             continue
    path = []
    return find_path_helper(grid,0,0,path,visited)

print(find_path(grid))





# Total number of paths from start to end
def total_paths(grid):
    paths = [[0]*len(grid[0]) for i in range(len(grid))]
    for i in range(len(grid[0])):
        if grid[0][i] == 0:
            break
        paths[0][i] = grid[0][i]
    for i in range(len(grid)):
        if grid[i][0] == 0:
            break
        paths[i][0] = grid[i][0]


    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            if grid[i][j] != 0:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
            else:
                paths[i][j] = 0
    return paths[-1][-1]

grid = [[1,1,1,1],
        [1,1,0,1],
        [0,1,1,1],
        [1,0,1,1]
    ]
print(total_paths(grid))
def dfs(i,j,grid,k,l):
    stack = [(i,j)]
    grid[i][j] = k
    while stack:
        x,y = stack.pop()
        for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
            new_x, new_y = x + direction[0], y + direction[1]
            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y]== l:
                grid[new_x][new_y]= k
                stack.append((new_x,new_y))
    return grid
            

def removeIslands(grid):
    # Write your code here.

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i == 0 or j == 0 or i == len(grid) -1 or j == len(grid[0]) -1):
                dfs(i,j,grid,2,1)
				
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i,j,grid,0,1)
    

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                dfs(i,j,grid,1,2)
    return grid

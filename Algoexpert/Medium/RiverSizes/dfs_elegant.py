def dfs(i,j):
    currentLength = 1
    stack = [(i,j)]
    grid[i][j] = '0'
    while stack:
        x,y = stack.pop()
        for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
            new_x, new_y = x + direction[0], y + direction[1]
            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y]=='1':
                currentLength += 1
                grid[new_x][new_y]= '0'
                stack.append((new_x,new_y))
    return currentLength
            
    

def numIsland(grid):
    lengthArray = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                a = dfs(i,j)
                lengthArray.append(a)
    return lengthArray

grid = [
  ["1","0","0","1","0"],
  ["1","0","0","1","0"],
  ["1","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(numIsland(grid))
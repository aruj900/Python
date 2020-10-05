from collections import deque

Directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

def shortestPath(grid):
    n = len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    queue = deque()
    queue.append((0,0,1))
    grid[0][0] = 1
    
    while len(queue):
        i,j,depth = queue.popleft()
        if i == n -1 and j == n -1:
            return depth
        for r,c in Directions:
            x = i + r
            y = j + c
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                grid[x][y] = 1
                queue.append((x,y,depth + 1))
    return -1


grid = [[0,1],[1,0]]

print(shortestPath(grid))
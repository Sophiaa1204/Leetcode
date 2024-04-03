#DFS
class Solution:
    def __init__(self):
        self.directions = [[-1,0],[1,0],[0,1],[0,-1]]
    
    def dfs(self,grid,x,y):
        rows = len(grid)
        columns = len(grid[0])

        if x < 0 or x >= rows or y < 0 or y >= columns:
            return 
        if grid[x][y] == "0":
            return 
        
        grid[x][y] = "0"

        for dx,dy in self.directions:
            new_x = x + dx
            new_y = y + dy
            self.dfs(grid,new_x,new_y)

    def numIslands(self,grid):
        rows = len(grid)
        columns = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid,i,j)
        
        return count
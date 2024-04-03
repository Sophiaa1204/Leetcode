# DFS
class Solution:
    def __init__(self):
        self.directions = [[-1,0],[1,0],[0,-1],[0,1]]

    def dfs(self,image,x,y,color,target):
        rows = len(image)
        columns = len(image[0])

        if x < 0 or x >= rows or y < 0 or y >= columns:
            return
        
        if image[x][y] != target or image[x][y] == color:
            return
        
        image[x][y] = color

        for dx,dy in self.directions:
            new_x, new_y = x + dx, y + dy
            self.dfs(image,new_x,new_y,color,target)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
       target = image[sr][sc]
       self.dfs(image,sr,sc,color,target)
       return image

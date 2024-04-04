# Backtrack
class Solution:
    def __init__(self):
        self.res = False
        self.directions = [[0,-1],[0,1],[-1,0],[1,0]]
        
    def backtrack(self, board, x, y, word, idx):
        rows = len(board)
        columns = len(board[0])

        if idx == len(word):
            self.res = True
            return
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return
        if self.visited[x][y]:
            return

        if board[x][y] == word[idx]:
            self.visited[x][y] = True    
            for dx,dy in self.directions:
                new_x, new_y = x + dx, y + dy
                self.backtrack(board, new_x, new_y, word, idx+1)
            self.visited[x][y] = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        self.visited = [[False for _ in range(columns)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(columns): 
                self.backtrack(board, i, j, word, 0)
                if self.res:
                    return True
        
        return self.res
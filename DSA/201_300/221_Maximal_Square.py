# 2D Dynamic Programming
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        max_len = 0

        dp = [[0 for _ in range(columns+1)] for _ in range(rows+1)]

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                    max_len = max(max_len,dp[i][j])
            
        return max_len * max_len
   
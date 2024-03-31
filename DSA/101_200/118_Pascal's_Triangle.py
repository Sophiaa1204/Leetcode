# DP
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [([0] * i) for i in range(1,numRows+1)]

        # Base Case
        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1
        
        for i in range(numRows):
            for j in range(i):
                if i != 0 and j != 0:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp
        
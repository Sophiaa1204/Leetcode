# 1D DP - from bottom to top
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP table
        dp = [0] * (n+1)
        # Base Case
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
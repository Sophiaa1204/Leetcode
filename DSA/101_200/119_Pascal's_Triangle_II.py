# Rotating DP
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        dp = [1,1]

        for i in range(1,rowIndex+2):
            curr = [0] * i
            for j in range(i):
                if j == 0 or j == i-1:
                    curr[j] = 1
                else:
                    curr[j] = dp[j-1] + dp[j]
            dp = curr
        
        return dp
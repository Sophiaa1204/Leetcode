# Triangle BP
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1000000] * i for i in range(1,len(triangle)+1)]
        # Base Case
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(1,len(triangle)):
            for j in range(i):
                if dp[i][j] != -1000000:
                    continue
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        # print(dp)
        return min(dp[len(triangle)-1])
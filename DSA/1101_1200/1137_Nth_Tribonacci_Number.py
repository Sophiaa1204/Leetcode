# DP - Memo
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0] * (n+1)

        return self.myTribonacci(memo,n)
    
    def myTribonacci(self,memo,n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        if memo[n] != 0:
            return memo[n]
        else:
            curr = self.myTribonacci(memo, n-3) + self.myTribonacci(memo, n-2) + self.myTribonacci(memo, n-1)
            memo[n] = curr
            return memo[n]
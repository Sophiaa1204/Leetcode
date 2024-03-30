# Backtrack - Combination
class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def backtrack(self,n,k,start):
        if len(self.track) == k:
            self.res.append(self.track[:])
            return
        
        for i in range(start,n+1):
            self.track.append(i)
            self.backtrack(n,k,i+1)
            self.track.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n,k,1)
        return self.res
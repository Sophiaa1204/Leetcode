# Backtrack - Combination, choose more than once
class Solution:
    def __init__(self):
        self.res = []
        self.track = []
    
    def backtrack(self,candidates,target,start):
        if sum(self.track) == target:
            self.res.append(self.track.copy())
            return
        if sum(self.track) > target:
            return
        
        for i in range(start,len(candidates)):
            self.track.append(candidates[i])
            self.backtrack(candidates,target,i)
            self.track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtrack(candidates,target,0)
        return self.res
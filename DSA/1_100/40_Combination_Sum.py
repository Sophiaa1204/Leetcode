# Backtrack - With Repeatation
class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.trackSum = 0
    
    def backtrack(self,candidates,target,start):
        if self.trackSum == target:
            self.res.append(self.track.copy())
            return
        if self.trackSum > target:
            return
        
        for i in range(start,len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            self.backtrack(candidates,target,i+1)
            self.track.pop()
            self.trackSum -= candidates[i]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates,target,0)
        return self.res